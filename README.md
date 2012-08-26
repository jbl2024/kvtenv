.. _README

Sample project for https://github.com/celery/billiard/issues/10

Instructions:

```sh
wget https://raw.github.com/pypa/virtualenv/master/virtualenv.py
./vtenv.sh
cd sample_project
./manage.py celery worker
```

Here is the output on my machine:

```sh
~/github/kvtenv/sample_project $ ./manage.py celery worker
------------------------------------------------------------------------------
 Manage in LOCAL mode : set DJANGO_MODE env variable for prod and dev servers.
 See README for more informations
------------------------------------------------------------------------------
/Users/blondon/github/kvtenv/vtenv/lib/python2.7/site-packages/djcelery/loaders.py:116: UserWarning: Using settings.DEBUG leads to a memory leak, never use this setting in production environments!
  warnings.warn("Using settings.DEBUG leads to a memory leak, never "
 
 -------------- celery@MacBook-Air-de-Jerome.local v3.0.7 (Chiastic Slide)
---- **** ----- 
--- * ***  * -- [Configuration]
-- * - **** --- . broker:      django://localhost//
- ** ---------- . app:         default:0x1043abb90 (djcelery.loaders.DjangoLoader)
- ** ---------- . concurrency: 4 (processes)
- ** ---------- . events:      OFF (enable -E to monitor this worker)
- ** ---------- 
- *** --- * --- [Queues]
-- ******* ---- . celery:      exchange:celery(direct) binding:celery
--- ***** ----- 

[2012-08-26 10:26:59,192: WARNING/MainProcess] celery@MacBook-Air-de-Jerome.local has started.
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ImportError: No module named billiard.forking
```
