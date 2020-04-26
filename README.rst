tfpy
====

.. image:: https://github.com/rgreinho/tfpy/workflows/ci/badge.svg

Create Terraform resources using Python.

Description
-----------

``tfpy`` is a thin wrapper around `terraformpy`_, aiming at providing a well defined
structure to organize your `terraform`_ stacks and leverage the power of Python to
define them rather than using `HCL`_.

The goal is to have a repository layout inspired from `Ansible <https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html#directory-layout>`_
where the stacks are driven by the variables.

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
  ├── generated
  │   └── commerce
  │       └── staging
  │           └── main.tf.json
  ├── library
  │   ├── backend.py
  │   └── provider.py
  ├── stacks
  │   └── commerce
  │       ├── README.md
  │       ├── gke.tf.py
  │       └── terraform.tf.py
  └── vars
      ├── all
      │   ├── cartigan.yml
      │   └── config.yml
      └── staging
          └── commerce
              ├── gke.yml
              └── project.yml

* ``generated``: folder where the stack are stored as JSON once generated.
* ``library``: folder where you can place custom functions.
* ``stacks``: the stacks created using TerraformPy.
* ``vars``: the variables used to create the stacks.

Examples
^^^^^^^^

Build a project stack without an environment::

  tfpy organization

Build a project stack for a specific environment::

  tfpy gke production


.. _HCL: https://github.com/hashicorp/hcl
.. _terraform: https://www.terraform.io
.. _terraformpy: https://github.com/NerdWalletOSS/terraformpy
