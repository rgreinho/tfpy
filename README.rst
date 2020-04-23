tfpy
====

.. image:: https://github.com/rgreinho/tfpy/workflows/ci/badge.svg

Create Terraform resources using Python.

Description
-----------

``tfpy`` is a thin wrapper around `terraformpy`_, aiming at providing a well defined
structure to organize your `terraform`_ stacks and leverage the power of Python to
define them rather than using `HCL`_.

For more information regarding how to create your stacks, please refer to the official
`terraformpy`_ documentation.

Installation
------------

tfpy requires Python 3.7+ to work

::

  pip install tfpy

Usage
-----

The ``tfpy`` command needs to be run at the root of your project.

The output will be created in a new subfolder within your project, named ``generated``.
For instance ``generated/gke/production/main.tf.json``

Project layout
^^^^^^^^^^^^^^

::

  .
  ├── stacks
  │   ├── gke
  │   │   └── main.tf.py
  │   ├── organization
  │   │   └── main.tf.py
  │   └── postgresql
  │       └── main.tf.py
  └── vars
      ├── all
      │   ├── config.yml
      │   ├── gke                   # Optional subfolder with the stack name to group
      │   │   └── gke.yml           # yaml files together if necessary.
      │   ├── organization.yml
      │   └── postgresql
      │       └── postgresql.yml
      ├── config,yml
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
