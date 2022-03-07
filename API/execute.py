from requests.utils import unquote
import os

def create_m_file(commands, id):
    with open('temp/' + str(id) + '.m', 'w') as f:
        f.write(commands)
        f.close()

def delete_m_file(id):
    os.remove('temp/' + str(id) + '.m')

def oct(commands, id):
    commands = str(unquote(commands))
    basecommand = "octave-cli --no-gui --no-history --no-init-file --no-init-path --no-line-editing --no-site-file --no-window-system -q "

    create_m_file(commands, id)

    run = os.popen(basecommand + 'temp/' + str(id) + '.m')
    toReturn = run.read().rsplit("\n", 1)[0]
    
    delete_m_file(id)

    return toReturn