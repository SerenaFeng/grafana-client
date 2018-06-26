Grafana-client
================

A project used to manage Grafana dashboards based on YAML configuration

YAML Specification
---------------------

The Grafana dashboard definitions are kept in any number of YAML files,
in whatever way you would like to organize them. When you invoke grafana-client
you may specify either the path of a single YAML file, or a directory.
If you choose a directory, all of the .yaml/.yml files in that directory will be read,
and all the dashboards they define will be created or updated.

Grafana-client through a few object types(dashboard, dashboard-template, project, macro,
default) to describe the dashboard.

.. note::
    Each object must be followed with a *name* definition right away. *name* is used
in parsing YAML blocks and objects, it is useless while rendering dashboard json body.

.. _Dashboard:

Dashboard
~~~~~~~~~~~~~~

The straightforward way to describe a dashboard. It looks like this:

.. code-block:: YAML

  - dashboard:
      name: directdb
      uid: directdb
      title: DirectDB Dashboard
      tags: [directdb]
      rows:
        - title: 'DirectDB Text'
          height: 100px
          panels:
            - title: 'DirectDB Text'
              type: text
              mode: html
              span: 12
              context: This a straightforward dashboard example

.. _Dashboard template:

Dashboard template
~~~~~~~~~~~~~~~~~~~~~

If several dashboards are nearly identical, except perhaps in their title, uid,
tags, etc., then you may use a Dashboard Template to specify the particulars of
the dashboard, and then use a Project_ to realize the dashboard with appropriate
variable substitution. Any variables not specified at the project level will be
inherited from the Defaults_

A Dashboard Template has the same syntax as a Dashboard_, but you may add variables
anywhere in the definition. Variables are indicated by enclosing them in braces,
e.g., {name} will substitute the variable name. When using a variable in a string
field, it is good practice to wrap the entire string in quotes, even if the rules
of YAML syntax don’t require it because the value of the variable may require quotes
after substitution.

You must include a variable in the name field of a Job Template (otherwise, every
instance would have the same name).

the following is dashboard template example:

.. code-block:: YAML

  - dashboard-template:
      name: 'db-{label}'
      uid: '{uid}'
      title: '{label} Dashboard'
      tags: '{tags}'
      rows:
        - title: '{label} Text'

.. _Project:

Project
~~~~~~~~~~~

The purpose of a project is to collect related dashboards together, and provide
values for the variables in a Dashboard Template. It looks like this:

.. code-block:: YAML

  - project:
      name: adb
      label: ADB
      description: This is dashboard test
      dashboards:
        - 'db-{label}':
            tags: [yaml, testcase]
            datasource: fake
            uid: '{name}'

If a variable is a list, the dashboard template will be realized with the variable
set to each value in the list. Multiple lists will lead to the template being
realized with the cartesian product of those values. Example:

.. code-block:: YAML

  - project:
      name: somedbs
      label:
        - SomeDBs-1
        - SomeDBs-2
      description: This is dashboard test
      dashboards:
        - 'db-{label}':
            tags: [somedbs]
            datasource: fake
            uid: '{label}'

.. _Macro:

Macro
~~~~~~~

Many of the rows or panels of a dashboard can be defined a a Macro, and then that
Macro used in the Dashboard_ description. The following YAML snippet defines a
Macro for *text panel*:

.. code-block:: YAML

  - macro:
      name: text_html_panel
      panels:
        - title: '{title} Text'
          type: text
          mode: html
          span: '{span}'
          context: '{context}'

  - dashboard:
      name: directdb
      uid: directdb
      title: DirectDB Dashboard
      tags: [directdb]
      rows:
        - title: 'DirectDB Text'
          height: 100px
          panels:
            - text_html_panel:
                title: DirectDB
                span: 12
                context: This is a macro example

.. _Defaults:

Defaults
~~~~~~~~~~~

Defaults collect dashboard attributes and will supply those values when the
dashboard is created, unless superseded by a value in the ‘Dashboard’_ definition.
If a set of Defaults is specified with the name global, that will be used by all
Dashboard (and Dashboard Template) definitions unless they specify a different
Default object with the defaults attribute. For example:

.. code-block:: YAML

  - defaults:
      name: global
      height: 100px

CLIs usage
---------------

Create dashboard
~~~~~~~~~~~~~~~~~~~~

.. code-block:: Shell

  grafana-client dashboard create -p path --conf config-file

``-p`` dashboard configuration path or filename

``--conf`` configuration file, where grafana_testapi URL and Grafana access authorization
is configured. If not provided, Grafana-client will look for it in the following order:

.. code-block:: Shell

  #. ~/.config/grafana_client/grafana_client.ini
  #. <script directory>/grafana_client.ini
  #. /etc/jenkins_jobs/grafana_client.ini

If None of the above is provided, the following configuration will be leveraged:

.. code-block:: INI

  [grafana_testapi]
  url = http://localhost:3000

  [grafana]
  authorization =
