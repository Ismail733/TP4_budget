import subprocess


def test():
    # Effectuez le test pour vérifier si le commit est bon ou mauvais.
    # Renvoyez True si le commit est bon, False sinon.
    pass


def bisect():
    # Démarrez le processus de bisect en spécifiant le commit initial qui est bon et mauvais.
    subprocess.check_call(['git', 'bisect', 'start', 'good_commit', 'bad_commit'])

    # Boucle jusqu'à ce que Git trouve le commit fautif.
    while True:
        # Obtenez le commit suivant à tester.
        subprocess.check_call(['git', 'bisect', 'next'])

        # Effectuez le test pour déterminer si le commit est bon ou mauvais.
        result = test()

        # Dites à Git si le commit est bon ou mauvais.
        if result:
            subprocess.check_call(['git', 'bisect', 'good'])
        else:
            subprocess.check_call(['git', 'bisect', 'bad'])

        # Si Git a trouvé le commit fautif, sortez de la boucle.
        if subprocess.check_output(['git', 'bisect', 'visualize']).strip() == b'':
            break

    # Affichez l'identifiant du commit fautif.
    subprocess.check_call(['git', 'log', '-1', '--pretty=%H'])
