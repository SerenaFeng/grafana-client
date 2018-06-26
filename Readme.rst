Grafana-client
================

A project used to manage Grafana dashboards based on YAML configuration

CLIs usage
---------------

Create dashboard
^^^^^^^^^^^^^^^^^^^^^

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


