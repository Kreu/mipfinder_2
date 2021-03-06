import unittest
import os

import sys
# Hacky way of doing it, for some reason relative imports don't work
<<<<<<< HEAD
sys.path.insert(0, "/home/troy/Documents/git/mipfinder2/mipfinder2")
=======
# sys.path.insert(0, "/media/troy/Data/Valdeko/documents/git/mipfinder2/mipfinder2")
>>>>>>> cf841dd97350ae61f6f9aca85eb462bcdfaa8ca7

import fasta


class TestextractFastaRecord (unittest.TestCase):

  def setUp(self):
    pass

  def test_valid_input(self):
    with open("test_fasta.txt", 'w') as f:
      f.write(">1\nTEST1\n")
      f.write(">2\nTEST2\n")
      f.write(">3\nTEST3\n")
      f.write(">4\nTEST4")
    
    expected_results = {">1": "TEST1",
                        ">2": "TEST2",
                        ">3": "TEST3",
                        ">4": "TEST4"
    }

    self.assertEqual(fasta.extractFastaRecords("test_fasta.txt"), expected_results)
    os.remove("test_fasta.txt")

  def test_extra_line_in_beginning(self):
    with open("test_fasta.txt", 'w') as f:
      f.write("Erroneous line\n")
      f.write(">1\nTEST1\n")
      f.write(">2\nTEST2\n")
      f.write(">3\nTEST3\n")
      f.write(">4\nTEST4")
    
    expected_results = {">1": "TEST1",
                        ">2": "TEST2",
                        ">3": "TEST3",
                        ">4": "TEST4"
    }

    self.assertEqual(fasta.extractFastaRecords("test_fasta.txt"), expected_results)
    os.remove("test_fasta.txt")

  def test_extra_line_in_end(self):
    with open("test_fasta.txt", 'w') as f:
      f.write("Erroneous line\n")
      f.write(">1\nTEST1\n")
      f.write(">2\nTEST2\n")
      f.write(">3\nTEST3\n")
      f.write(">4\nTEST4")
    
    expected_results = {">1": "TEST1",
                        ">2": "TEST2",
                        ">3": "TEST3",
                        ">4": "TEST4"
    }

    self.assertEqual(fasta.extractFastaRecords("test_fasta.txt"), expected_results)
    os.remove("test_fasta.txt")


class TestgetProteinExistenceLevel (unittest.TestCase):

  def setUp(self):
    self.level_one= ">sp|Q9C5U0|AHK4_ARATH Histidine kinase 4 OS=Arabidopsis thaliana OX=3702 GN=AHK4 PE=1 SV=1"
    self.level_five = ">sp|Q9C5U0|AHK4_ARATH Histidine kinase 4 OS=Arabidopsis thaliana OX=3702 GN=AHK4 PE=5 SV=4"
    self.no_protein_level = ">sp|Q9C5U0|AHK4_ARATH Histidine kinase 4 OS=Arabidopsis thaliana OX=3702 GN=AHK4 SV=4"

  def test_level_one(self):
    self.assertEqual(fasta.getProteinExistenceLevel(self.level_one), 1)

  def test_level_five(self):
    self.assertEqual(fasta.getProteinExistenceLevel(self.level_five), 5) 

  def test_no_level(self):
    self.assertEqual(fasta.getProteinExistenceLevel(self.no_protein_level), -1)


class TestextractUniprotID (unittest.TestCase):

  def setUp(self):
    self.fasta_header = ">sp|Q9C5U0|AHK4_ARATH Histidine kinase 4 OS=Arabidopsis thaliana OX=3702 GN=AHK4 PE=1 SV=1"
    self.expected_output = "Q9C5U0"

  def test_uniprot_kb_header(self):
    self.assertEqual(fasta.extractUniprotID(self.fasta_header, 3), self.expected_output)