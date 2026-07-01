#coding:utf8
import unittest
from .creature import Spider, Creature



class TestChemicalProperties(unittest.TestCase): 

  # Reactions between the reagents
  # TODO: check test before first start, and do in after creating source of classes Creature: and Spider:
  def test_add_connection(self):
    spider = Spider()
    # Programm to creating molecules 
    creating_molecular_spider = spider.init(chemical=[
      (
        [(13, 13), (13, 13)], 
       [(17, 17), (17, 17), (17, 17)]
      ), 
    ),
    # Program to creating microuniverse-space to molecular reactions 
    creating_micro_universe_space_reactions = spider.init(perimeter=(100,100,100), chemical =
                    [
                      (
                       (13, 17), (13, 17), (13, 17)
                      ), 
                      (
                       (13, 17), (13, 17), (13, 17)
                      )
                    ]
                   )
    
    creature = Creature(spider)
    connections = creature.get_connections() 
    ```
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
    ```



