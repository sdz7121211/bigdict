# coding: utf-8
from os import path
import os
import uuid
import time
import bsddb
try:
    import cPickle as pickle
except ImportError:
    import pickle

__author__ = "sudz"
__email__ = "670108918@qq.com"


class bigdict:

    def __init__(*args, **kwargs):

        if not args:
            raise TypeError("descriptor '__init__' of 'bigdict' object "
                            "needs an argument")
        self = args[0]
        self._initcache()
        args = args[1:]
        if len(args) > 1:
            raise TypeError('expected at most 1 arguments, got %d' % len(args))
        if args:
            dict = args[0]
        elif 'dict' in kwargs:
            dict = kwargs.pop('dict')
            import warnings
            warnings.warn("Passing 'dict' as keyword argument is "
                          "deprecated", PendingDeprecationWarning,
                          stacklevel=2)
        else:
            dict = None

        if dict is not None:
            self.update(dict)
        if len(kwargs):
            self.update(kwargs)

    def _initcache(self):
        self._id = "".join([uuid.uuid4().hex, time.strftime("%Y%m%d%H%M%S")])
        self._cache_path = path.dirname(__file__)
        assert path.exists(self._cache_path)
        self.data = bsddb.btopen(os.path.join(self._cache_path, self._id), "n")

    def __repr__(self):
        return repr(dict(zip(self.keys(), self.values())))

    def __cmp__(self, dict):
        if isinstance(dict, bigdict):
            return cmp(self.data, dict.data)
        else:
            return cmp(self.data, dict)

    __hash__ = None  # Avoid Py3k warning

    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        _key = pickle.dumps(key, 2)
        # print "key", key, _key
        if self.data.has_key(_key):
            return pickle.loads(self.data[_key])
        if hasattr(self.__class__, "__missing__"):
            return self.__class__.__missing__(self, key)
        raise KeyError(_key)

    def __setitem__(self, key, item):
        _key = pickle.dumps(key, 2)
        self.data[_key] = pickle.dumps(item, 2)

    def __delitem__(self, key):
        _key = pickle.dumps(key, 2)
        if not self.data.has_key(_key):
            raise KeyError(key)
        del self.data[_key]

    def __del__(self):
        if hasattr(self, 'data'):
            self.data.close()
            os.remove(os.path.join(self._cache_path, self._id))

    def __contains__(self, key):
        _key = pickle.dumps(key, 2)
        return self.data.has_key(_key)

    def __iter__(self):
        for key in self.iterkeys():
            yield key

    def clear(self):
        if hasattr(self, 'data'):
            self.data.close()
            self.data = bsddb.btopen(os.path.join(self._cache_path, self._id), "n")

    def copy(self):
        raise AttributeError

    def keys(self):
        return map(pickle.loads, self.data.keys())

    def values(self):
        return map(pickle.loads, self.data.values())

    def items(self):
        return zip(self.keys(), self.values())

    def iteritems(self):
        for k, v in self.data.iteritems():
            yield (pickle.loads(k), pickle.loads(v))

    def iterkeys(self):
        for k, v in self.data.iteritems():
            yield pickle.loads(k)

    def itervalues(self):
        for k, v in self.data.iteritems():
            yield pickle.loads(v)

    def has_key(self, key):
        _key = pickle.dumps(key, 2)
        return self.data.has_key(_key)

    def update(*args, **kwargs):
        if not args:
            raise TypeError("descriptor 'update' of 'bigdict' object "
                            "needs an argument")
        self = args[0]
        args = args[1:]
        if len(args) > 1:
            raise TypeError('expected at most 1 arguments, got %d' % len(args))

        if args:
            dict = args[0] # set bigdict/dict/bsddb as dict
        elif 'dict' in kwargs:
            dict = kwargs.pop('dict')
            import warnings
            warnings.warn("Passing 'dict' as keyword argument is deprecated",
                          PendingDeprecationWarning, stacklevel=2)
        else:
            dict = None

        if dict is None:
            pass
        elif isinstance(dict, bigdict):
            for k, v in dict.iteritems():
                self.data[pickle.dumps(k)] = pickle.dumps(v)
        elif isinstance(dict, type({})):
            for k, v in dict.iteritems():
                self[k] = v
        if len(kwargs):
            self.update(kwargs)

    def get(self, key, failobj=None):
        _key = pickle.dumps(key, 2)
        if not self.data.has_key(_key):
            return failobj
        return pickle.loads(self.data[_key])

    def setdefault(self, key, failobj=None):
        _key = pickle.dumps(key, 2)
        if _key not in self.data:
            self.data[_key] = pickle.dumps(failobj, 2)
        return pickle.loads(self.data[_key])

    def pop(self, key, *args):
        _key = pickle.dumps(key, 2)
        if not self.data.has_key(_key):
            raise KeyError(key)
        value = self.data[_key]
        del self.data[_key]
        return pickle.loads(value)

    def popitem(self):
        key, value = None, None
        for k, v in self.data.iteritems():
            key, value = k, v
            break
        del self.data[key]
        return (pickle.loads(key), pickle.loads(value))

    @classmethod
    def fromkeys(cls, iterable, value=None):
        d = cls()
        for key in iterable:
            _key = pickle.dumps(key, 2)
            d[_key] = pickle.dumps(value, 2)
        return d


