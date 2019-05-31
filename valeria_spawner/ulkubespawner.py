from jinja2 import Template
from kubespawner import KubeSpawner

class ULKubeSpawner(KubeSpawner):
    def _options_form_default(self):
        with open('/opt/app-root/src/templates/select.html') as file_:
            template = Template(file_.read())
        image_list = ['s2i-minimal-notebook-s3:3.6', 
                      's2i-scipy-notebook-s3:3.6', 
                      's2i-tensorflow-notebook-s3:3.6',
                      's2i-tensorflow-exp-s3:3.6',
                      's2i-minimal-notebook:3.6',
                     's2i-pyspark-notebook-s3:3.6',
                     's2i-spark-minimal-notebook:3.6',
                     's2i-spark-scipy-notebook:3.6',
                     'jupyter-notebooks-s3:latest']
        return template.render(image_list=image_list)

    def options_from_form(self, formdata):
        try:
            self.cpu_limit = float(formdata.get('cpu_limit')[0])
            self.mem_limit = formdata.get('mem_limit')[0] + 'M'
            self.image_spec = formdata.get('image_spec')[0]
        except:
            raise Exception(str(formdata))

        if 'jupyterlab' in formdata.get('options', []):
            self.cmd = ['jupyter-labhub']
            self.default_url = '/lab'
        
        return formdata
