tfpy
====

.. image:: https://github.com/shipstation/octopy/workflows/ci/badge.svg

Create Terraform resources using Python

Description
-----------

``tfpy`` is a thin wrapper around `terraformpy`_, aiming at providing a well defined
structure to organize your `terraform`_ stacks and leverage the power of Python to
define them rather than using `HCL_`.

Installation
------------

tfpy requires Python 3.7+ to work

::

  pip install scrapd

Usage
-----

Project layout
^^^^^^^^^^^^^^

::

  .
  ├── stacks
  │   ├── gke
  │   │   └── main.tf.py
  │   └── postgresql
  │       └── main.tf.py
  └── vars
      ├── all
      │   ├── config.yml
      │   ├── gke                   # Subfolder with the stack name to group yaml files
      │   │   └── gke.yml           # together if necessary.
      │   └── postgresql
      │       └── postgresql.yml
      ├── production
      │   ├── gke
      │   │   └── gke.yml
      │   └── postgresql
      │       └── postgresql.yml
      └── staging
          ├── gke
          │   └── gke.yml
          └── postgresql
              └── postgresql.yml

Examples
^^^^^^^^

Build a stack without an environment::

  tfpy organization

Build a stack for a specific environment::

  tfpy gke production


.. _HCL: https://github.com/hashicorp/hcl
.. _terraform: https://www.terraform.io
.. _terraformpy: https://github.com/NerdWalletOSS/terraformpy
