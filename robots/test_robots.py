#coding:utf8
import unittest
from .creature import Spider, Creature



class TestChemicalProperties: 

  # Reactions between the reagents
  # TODO: check test before first start, and do in after creating source of classes Creature: and Spider:
  def test_add_connection(self):
    self.assertEqual(Creature(Spider(chemical=[
      (
        [(13, 13), (13, 13)], 
       [(17, 17), (17, 17), (17, 17)]
      ), 
    ]), perimeter=(100,100,100)), 
                    [
                      (
                       (13, 17), (13, 17), (13, 17)
                      ), 
                      (
                       (13, 17), (13, 17), (13, 17)
                      )
                    ]
      )

