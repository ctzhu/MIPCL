from mipcl_py.mipshell.mipshell import *

class CorporateStructure(Problem):
    """Corporate structure optimization for multinational companies.

    Given list, named Country, of n countries.
    For each country i we know:
        Country[i]['taxRule'] in {E,D,S,M}:
            E means exemption tax-relief rule;
            D means deduction tax-relief rule;
            S means source by source income pooling, credit tax-relief rule;
            W means world-wide income polling, credit tax-relief rule;
        Country[i]['foreignTax']: foreign income tax rate (fraction);
        Country[i]['domesticTax']: domestic income tax rate (fraction);
        Country[i]['profit']: profit generated at country i:
            countries where the profit is greater than zero must be in the tax tree,
            while countries where the profit is zero (non-source countries) may (or may not) be in the tax teree;
        Country[i]['withholdingTax'][j]: withholding tax rate (fraction) from country i to country j.
    """
    def model(self,t,Country): 
        def r(i): return Country[i]['profit']
        def d(i): return Country[i]['domesticTax']
        def h(i): return Country[i]['foreignTax']
        def g(i,j): return Country[i]['withholdingTax'][j]
        def inc(i): return [j for j in range(n) if i in out(j)]
        def out(i):
            if (i != t): return Country[i]['withholdingTax'].keys()
            else: return [] 
            

        self.t = t
        self.Country = Country
        n = len(Country)
        R0 = sum(r(i) for i in range(n))
        Q = min((1.0-d(i)) * (1.0 - max(g(i,j) for j in out(i))) for i in range(n) if i != t)

        self.p = p = VarVector((n,),'p')
        f, f0 = {}, {}
        for i in range(n):
            f[i], f0[i] = {}, {}
            if i != t:
                for j in out(i):
                    f[i][j], f0[i][j] = Var('f({:},{:})'.format(i,j)), Var('f0({:},{:})'.format(i,j))
                
        self.f, self.f0 = f, f0

        u = [{} for j in range(n)]

        maximize(sum_((1.0-g(i,t))*f[i][t] for i in inc(t)) - p[t])

        for i in range(n):
            taxRule = Country[i]['taxRule'] 
            if i != t:
                for j in out(i):
                    f[i][j] <= f0[i][j]
                    f0[i][j] <= ((1.0-g(i,j))/Q)*f[i][j]    
                if len(out(i)) > 1: (sum_(f[i][j] for j in out(i)) <= R0).setType(SOS1)
                sum_(f0[i][j] for j in out(i)) - sum_(f0[j][i] for j in inc(i)) == r(i)
                sum_(f[i][j] for j in out(i)) - sum_((1.0-g(j,i))*f[j][i] for j in inc(i)) == r(i) - p[i]
            if taxRule == 'E':
                p[i] == d(i)*r(i)
            elif taxRule == 'D':
                p[i] == d(i)*r(i) + sum_(h(i)*(1.0-g(j,i))*f[j][i] for j in inc(i))
            elif taxRule == 'W':
                p[i] >= d(i)*r(i)
                p[i] >= d(i)*r(i) + sum_((1.0-g(j,i))*f[j][i] for j in inc(i))\
                                  - sum_((1.0-h(i))*f0[j][i] for j in inc(i))
            else:# taxRule == 'S':
                for j in inc(i):
                    u[j][i] = Var('u({:d},{:d})'.format(j,i))
                    u[j][i] >= (1.0-g(j,i))*f[j][i] - (1.0-h(i))*f0[j][i]
                p[i] == d(i)*r(i) + sum_(u[j][i] for j in inc(i))

#        self._print()
  
    def printSolution(self):
        def out(i): return Country[i]['withholdingTax'].keys()
        Country, t = self.Country, self.t
        n = len(Country)
        p, f, f0 = self.p, self.f, self.f0
        print('Holding company income = {:.2f}'.format(Country[t]['profit'] + self.getObjVal()))
        print('Tax tree')
        print('=========================================')     
        print('Country  Parent         Flow     Tax Paid')
        print('=========================================')     
        for i in range(n):
            if i != t:
                parent=-1
                for j in out(i):
                    if f0[i][j].val > 0.5:
                        parent = j
                        break
                if parent >= 0:
                    print(' {:6d}   {:5d}  {:11.2f}   {:10.2f}'.format(i+1,parent+1,f[i][j].val,p[i].val))
            else:
                print(' {:6d}       -                {:10.2f}'.format(i+1,p[i].val))
        print('=========================================')     
 #       for i in range(n):
 #           for j in range(n):
 #               if f0[i][j].val > 0.01:
 #                   print('f0({:d},{:d})={:2f}'.format(i+1,j+1,f0[i][j].val))
 #       print('=========================================')     

