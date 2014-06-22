import json
import sys, time
import subprocess

deploymentInfo = json.loads(sys.stdin.read())
deploymentId = deploymentInfo['deploymentId']

def probe(deploymentId):
  result = json.loads(subprocess.check_output(['aws', 'deploy', 'get-deployment', '--deployment-id', deploymentId]))
  return result['deploymentInfo']['status']

while True:
  status = probe(deploymentId)
  if status == 'Failed':
      print 'Deployment failed'
      sys.exit(1)
  elif status == 'Succeeded':
      print 'Deployment succeeded'
      sys.exit()
  else:
      print 'Deployment in progress. Waiting...'
      time.sleep(5)
