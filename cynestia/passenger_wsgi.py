import sys, os
ApplicationDirectory = '/var/www/vhosts/cynestia.com/httpdocs/cynestia_venv/cynestia-web' 
ApplicationName = 'Cynestia-Web' 
VirtualEnvDirectory = '/var/www/vhosts/cynestia.com/httpdocs/cynestia_venv' 
VirtualEnv = os.path.join(os.getcwd(), VirtualEnvDirectory, 'bin', 'python') 
if sys.executable != VirtualEnv: os.execl(VirtualEnv, VirtualEnv, *sys.argv) 
sys.path.insert(0, os.path.join(os.getcwd(), ApplicationDirectory)) 
sys.path.insert(0, os.path.join(os.getcwd(), ApplicationDirectory, ApplicationName)) 
sys.path.insert(0, os.path.join(os.getcwd(), VirtualEnvDirectory, 'bin')) 
os.chdir(os.path.join(os.getcwd(), ApplicationDirectory)) 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', ApplicationName + '.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()