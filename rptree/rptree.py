# rptree.py

"""This module provides RP Tree main module."""

import os
import pathlib

PIPE = "│"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "


class TreeDictionary:
    def __init__(self, root_dir):
        self._generator = _TreeGenerator(root_dir)
        
    def generate(self):
        tree = self._generator.build_tree()
        for entry in tree:
            print(entry)


class _TreeGenerator:
    def __init__(self, root_dir):
        self._root_dir = pathlib.Path(root_dir)
        self._tree = []
        
    def build_tree(self):
        self._tree_head()
        self._tree_body(self._root_dir)
        return self._tree
    
    def _tree_head(self):
        self._tree.append(f"{self._root_dir}{os.sep}")
        self._tree.append(PIPE)
    
    def _tree_body(self, dictionary, prefix=""):
        entries = dictionary.iterdir()
        entries = sorted(entries, key= lambda entry: entry.is_file())
        total_entries = len(entries)
        for index, entry in enumerate(entries):
            Connector = ELBOW if index==(total_entries-1) else TEE
            if entry.isdir():
                self._add_dictionary(index, total_entries, dictionary, prefix, Connector)
            else:
                self._add_file(entry, prefix, Connector)
    
                
    def _add_dictionary(self, index, total_entries, dictionary, prefix, Connector):
        self._tree.append(f"{prefix}{Connector} {dictionary.name}{os.sep}")
        if index != total_entries-1:
            prefix += PIPE_PREFIX
        else:
            prefix += SPACE_PREFIX
        self._tree_body(dictionary= dictionary, prefix= prefix)
        self._tree.append(prefix.rstrip())
    
    def _add_file(self, file, prefix, Connector):
        self._tree.append(f"{prefix}{Connector} {file.name}")        
                
        
        
        
        
        