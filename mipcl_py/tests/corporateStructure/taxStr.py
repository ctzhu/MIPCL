#!/usr/bin/python

from mipcl_py.models.corporateStructuring import CorporateStructure

target = 0
Countries = (
    {
         'Name': '0',
         'taxRule': 'S', 'domesticTax': 0.35, 'foreignTax': 0.35, 'profit': 103,
         'withholdingTax': {
              1: 0.00, 2: 0.15, 3: 0.00, 4: 0.00, 5: 0.00, 6: 0.25, 7: 0.00, 8: 0.10, 9: 0.00, 10: 0.00,
              11: 0.00, 12: 0.00, 13: 0.25, 14: 0.00, 15: 0.25, 16: 0.10, 17: 0.10, 18: 0.25, 19: 0.10
         }
    },
    {
         'Name': '1',
         'taxRule': 'E', 'domesticTax': 0.35, 'foreignTax': 0.0, 'profit': 0.0,
         'withholdingTax': {
              0: 0.00, 2: 0.15, 3: 0.00, 4: 0.00, 5: 0.00, 6: 0.15, 7: 0.00, 8: 0.00, 9: 0.00, 10: 0.00,
              11: 0.00, 12: 0.00, 13: 0.25, 14: 0.00, 15: 0.25, 16: 0.05, 17: 0.10, 18: 0.10, 19: 0.00
         }
    },
    {
         'Name': '2',
         'taxRule': 'D', 'domesticTax': 0.33, 'foreignTax': 0.33, 'profit': 522,
         'withholdingTax': {
              0: 0.00, 1: 0.00, 3: 0.00, 4: 0.00, 5: 0.00, 6: 0.00, 7: 0.00, 8: 0.00, 9: 0.00, 10: 0.00,
              11: 0.00, 12: 0.00, 13: 0.00, 14: 0.00, 15: 0.00, 16: 0.00, 17: 0.00, 18: 0.00, 19: 0.00
         }
    },
    {
         'Name': '3',
         'taxRule': 'S', 'domesticTax': 0.35, 'foreignTax': 0.35, 'profit': 0.0,
         'withholdingTax': {
              0: 0.00, 1: 0.00, 2: 0.15, 4: 0.00, 5: 0.00, 6: 0.25, 7: 0.00, 8: 0.10, 9: 0.00, 10: 0.00,
              11: 0.00, 12: 0.00, 13: 0.25, 14: 0.00, 15: 0.25, 16: 0.10, 17: 0.10, 18: 0.25, 19: 0.10
         }
    },
    {
         'Name': '4',
         'taxRule': 'S', 'domesticTax': 0.33, 'foreignTax': 0.33, 'profit': 0.0,
         'withholdingTax': {
              0: 0.05, 1: 0.05, 2: 0.05, 3: 0.05, 5: 0.05, 6: 0.05, 7: 0.05, 8: 0.05, 9: 0.05, 10: 0.05,
              11: 0.05, 12: 0.05, 13: 0.05, 14: 0.05, 15: 0.05, 16: 0.05, 17: 0.05, 18: 0.05, 19: 0.05
         }
    },
    {
         'Name': '5',
         'taxRule': 'E', 'domesticTax': 0.35, 'foreignTax': 0.0, 'profit': 0.0,
         'withholdingTax': {
              0: 0.00, 1: 0.00, 2: 0.15, 3: 0.00, 4: 0.00, 6: 0.15, 7: 0.00, 8: 0.00, 9: 0.00, 10: 0.00,
              11: 0.00, 12: 0.00, 13: 0.25, 14: 0.00, 15: 0.25, 16: 0.05, 17: 0.10, 18: 0.10, 19: 0.00
         }
    },
    {
         'Name': '6',
         'taxRule': 'E', 'domesticTax': 0.33, 'foreignTax': 0.0, 'profit': 205,
         'withholdingTax': {
              0: 0.30, 1: 0.15, 2: 0.15, 3: 0.30, 4: 0.15, 5: 0.15, 7: 0.15, 8: 0.15, 9: 0.15, 10: 0.30,
              11: 0.15, 12: 0.30, 13: 0.30, 14: 0.15, 15: 0.30, 16: 0.15, 17: 0.15, 18: 0.15, 19: 0.15
         }
    },
    {
         'Name': '7',
         'taxRule': 'W', 'domesticTax': 0.4, 'foreignTax': 0.2, 'profit': 136,
         'withholdingTax': {
              0: 0.00, 1: 0.00, 2: 0.15, 3: 0.00, 4: 0.00, 5: 0.00, 6: 0.15, 8: 0.10, 9: 0.00, 10: 0.00,
              11: 0.00, 12: 0.00, 13: 0.25, 14: 0.00, 15: 0.25, 16: 0.05, 17: 0.10, 18: 0.10, 19: 0.05
         }
    },
    {
         'Name': '8',
         'taxRule': 'E', 'domesticTax': 0.1, 'foreignTax': 0.0, 'profit': 0.0,
         'withholdingTax': {
              0: 0.10, 1: 0.00, 2: 0.15, 3: 0.10, 4: 0.05, 5: 0.00, 6: 0.15, 7: 0.10, 9: 0.05, 10: 0.00,
              11: 0.00, 12: 0.00, 13: 0.15, 14: 0.05, 15: 0.35, 16: 0.05, 17: 0.10, 18: 0.10, 19: 0.05
         }
    },
    {
         'Name': '9',
         'taxRule': 'E', 'domesticTax': 0.33, 'foreignTax': 0.0, 'profit': 336,
         'withholdingTax': {
              0: 0.00, 1: 0.00, 2: 0.15, 3: 0.00, 4: 0.00, 5: 0.00, 6: 0.15, 7: 0.00, 8: 0.05, 10: 0.00,
              11: 0.00, 12: 0.00, 13: 0.25, 14: 0.00, 15: 0.25, 16: 0.05, 17: 0.10, 18: 0.10, 19: 0.05
         }
    },
    {
         'Name': '10',
         'taxRule': 'E', 'domesticTax': 0.35, 'foreignTax': 0.0, 'profit': 108,
         'withholdingTax': {
              0: 0.00, 1: 0.00, 2: 0.00, 3: 0.00, 4: 0.00, 5: 0.00, 6: 0.00, 7: 0.00, 8: 0.00, 9: 0.00,
              11: 0.00, 12: 0.00, 13: 0.00, 14: 0.00, 15: 0.00, 16: 0.00, 17: 0.00, 18: 0.00, 19: 0.00
         }
    },
    {
         'Name': '11',
         'taxRule': 'D', 'domesticTax': 0.28, 'foreignTax': 0.28, 'profit': 119,
         'withholdingTax': {
              0: 0.00, 1: 0.00, 2: 0.15, 3: 0.00, 4: 0.00, 5: 0.00, 6: 0.15, 7: 0.00, 8: 0.00, 9: 0.00,
              10: 0.00, 12: 0.00, 13: 0.15, 14: 0.00, 15: 0.30, 16: 0.05, 17: 0.10, 18: 0.10, 19: 0.00
         }
    },
    {
         'Name': '12',
         'taxRule': 'E', 'domesticTax': 0.35, 'foreignTax': 0.0, 'profit': 97,
         'withholdingTax': {
              0: 0.00, 1: 0.00, 2: 0.00, 3: 0.00, 4: 0.00, 5: 0.00, 6: 0.00, 7: 0.00, 8: 0.00, 9: 0.00,
              10: 0.00, 11: 0.00, 13: 0.00, 14: 0.00, 15: 0.00, 16: 0.00, 17: 0.00, 18: 0.00, 19: 0.00
         }
    },
    {
         'Name': '13',
         'taxRule': 'D', 'domesticTax': 0.33, 'foreignTax': 0.33, 'profit': 27,
         'withholdingTax': {
              0: 0.27, 1: 0.27, 2: 0.27, 3: 0.27, 4: 0.05, 5: 0.27, 6: 0.27, 7: 0.27, 8: 0.05, 9: 0.05,
              10: 0.27, 11: 0.00, 12: 0.27, 14: 0.00, 15: 0.27, 16: 0.05, 17: 0.27, 18: 0.27, 19: 0.00
         }
    },
    {
         'Name': '14',
         'taxRule': 'D', 'domesticTax': 0.28, 'foreignTax': 0.28, 'profit': 313,
         'withholdingTax': {
              0: 0.00, 1: 0.00, 2: 0.15, 3: 0.00, 4: 0.00, 5: 0.00, 6: 0.15, 7: 0.00, 8: 0.00, 9: 0.00,
              10: 0.00, 11: 0.00, 12: 0.00, 13: 0.00, 15: 0.28, 16: 0.05, 17: 0.10, 18: 0.10, 19: 0.00
         }
    },
    {
         'Name': '15',
         'taxRule': 'W', 'domesticTax': 0.17, 'foreignTax': 0.17, 'profit': 38,
         'withholdingTax': {
              0: 0.00, 1: 0.00, 2: 0.00, 3: 0.00, 4: 0.00, 5: 0.00, 6: 0.00, 7: 0.00, 8: 0.00, 9: 0.00,
              10: 0.00, 11: 0.00, 12: 0.00, 13: 0.00, 14: 0.00, 16: 0.00, 17: 0.00, 18: 0.00, 19: 0.00
         }
    },
    {
         'Name': '16',
         'taxRule': 'W', 'domesticTax': 0.35, 'foreignTax': 0.35, 'profit': 435,
         'withholdingTax': {
              0: 0.10, 1: 0.05, 2: 0.15, 3: 0.10, 4: 0.05, 5: 0.05, 6: 0.15, 7: 0.05, 8: 0.05, 9: 0.05,
              10: 0.05, 11: 0.05, 12: 0.05, 13: 0.05, 14: 0.05, 15: 0.30, 17: 0.10, 18: 0.15, 19: 0.15
         }
    },
    {
         'Name': '17',
         'taxRule': 'D', 'domesticTax': 0.24, 'foreignTax': 0.24, 'profit': 411,
         'withholdingTax': {
              0: 0.00, 1: 0.00, 2: 0.00, 3: 0.00, 4: 0.00, 5: 0.00, 6: 0.00, 7: 0.00, 8: 0.00, 9: 0.00,
              10: 0.00, 11: 0.00, 12: 0.00, 13: 0.00, 14: 0.00, 15: 0.00, 16: 0.00, 18: 0.00, 19: 0.00
         }
    },
    {
         'Name': '18',
         'taxRule': 'D', 'domesticTax': 0.45, 'foreignTax': 0.45, 'profit': 143,
         'withholdingTax': {
              0: 0.20, 1: 0.10, 2: 0.15, 3: 0.20, 4: 0.10, 5: 0.10, 6: 0.15, 7: 0.15, 8: 0.10, 9: 0.10,
              10: 0.10, 11: 0.15, 12: 0.10, 13: 0.20, 14: 0.10, 15: 0.20, 16: 0.15, 17: 0.20, 19: 0.15
         }
    },
    {
         'Name': '19',
         'taxRule': 'D', 'domesticTax': 0.28, 'foreignTax': 0.28, 'profit': 320,
         'withholdingTax': {
              0: 0.10, 1: 0.00, 2: 0.15, 3: 0.10, 4: 0.05, 5: 0.00, 6: 0.15, 7: 0.05, 8: 0.05, 9: 0.05,
              10: 0.05, 11: 0.00, 12: 0.05, 13: 0.00, 14: 0.00, 15: 0.25, 16: 0.15, 17: 0.15, 18: 0.15
         }
    },
)

prob = CorporateStructure('taxStr')
prob.model(target,Countries)
prob.optimize(False)
prob.printSolution()
