# SOK
Student: Bogdan Janosevic SV65/2020

## HOW TO START A PROGRAM:

1. First of all, you need to install Django:
2. pip install django
3. 
4. Activate the virtual environment.

5. Navigate to the SOK folder.

6. Follow these commands:

```bash
cd core
python setup.py install
cd ..
cd SimpleDataVisualizer
pip uninstall simple_data_visualizer
y
python setup.py install
cd ..
cd DataProviderXML 
pip uninstall data_provider_xml
python setup.py install
cd ..
cd sok_project
python manage.py runserver
