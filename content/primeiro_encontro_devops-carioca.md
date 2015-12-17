Title: Primeiro encontro do DevOps Carioca!
Date: 2015-12-16 12:00
Category: Python
Tags: pelican, markdown
Slug: primeiro-artigo
Author: Diogo Leal
Summary: Um resumo sobre o primeiro encontro do DevOps Carioca

Antes de começar a falar como foi o encontro, é importante explicar como surgiu o DevOps Carioca.

A idéia surgiu em um hands-on sobre Docker em um domingo no Shopping New York, realizado pelo Hugo Leonardo. Esse encontro foi tão bacana, que além de falarmos sobre Docker, falamos sobre ferramenta de testes, deploy e outras tecnologias de ponta. Mas o conhecimento foi compartilhado para poucas pessoas, e então sentimos a necessidade da criação de um grupo, onde seria possível, ao mesmo, compartilhar e aprender.

E para iniciar um grupo, nada melhor que um encontro, não é mesmo?

Assim marcamos o encontro na sede da [InfoLink](http://infolink.com.br) para o dia 2 de Dezembro.

## Como foi o encontro?

Resumindo em uma palavra: <b>Sensacional!</b>

Enquanto as pessoas chegavam, discutimos sobre diversos assuntos. O Hugo apresentou o [Exercism](http://exercism.io/), um site onde você pratica exercícios e outras pessoas fazem comentários sobre a forma como você resolveu o problema. Ninguém lembra como, mas emendamos numa conversa interessante sobre [Systemd](http://freedesktop.org/wiki/Software/systemd/), [System V](https://en.wikipedia.org/wiki/UNIX_System_V), [runit](http://smarden.org/runit/) e outras alternativas e no final disso debatemos sobre as funcionalidades do [Tmux](https://tmux.github.io/).

O [Hugo](https://github.com/hugoleodev) foi o mestre de cerimônias, ele falou sobre o funcionamento do [Testinfra](https://testinfra.readthedocs.org/en/latest/) e de como é possível integrar a ferramenta com o Docker e em pouco tempo começamos um coding dojo usando essas duas ferramentas.

Definimos que subiríamos o Flask no Docker, testando se o Python está instalado até a execução do Flask. Os testes definidos podem ser visto [aqui] (https://github.com/DevOpsCarioca/dojo-testinfra/blob/master/container_flask.txt)

Para quem nunca ouviu falar do TestInfra: Ele é uma ferramenta que faz teste na infra. Por exemplo, ele verifica se uma aplicação está no ar, se um programa está instalado, se um arquivo existe, etc. E os testes são bem simples:

```
def test_python_version(Package):
    python = Package("python2.7")
    assert python.version.startswith("2.7")
```
Essa é uma função que testa se o pacote Python está com a versão 2.7 instalada. Ele é recomendável para testes após deploy e além da comunicação com o Docker, ele consegue se comunicar por enquanto com a sua máquina local, com o Paramiko, ssh, salt e Ansible.

O excelente papo, compartilhamento de conhecimento e pessoas legais, foram regados com bolos, biscoitos, sanduíches, sucos e é claro, as deliciosas pipocas de microondas feitas pela [Darlene](https://github.com/darlenedms).

![Foto do primeiro encontro](/images/primeiro_encontro_02_12.jpg)

Durante o encontro o [Hugo](https://github.com/hugoleodev) e o [Souza](https://github.com/chevectra87) [assumiram uma issue](https://github.com/philpep/testinfra/issues/24)
no Testinfra, para implantar um módulo para os processos.

Com tanta energia positiva, é claro que no final do encontro, conseguimos criar todos os testes que foram definidos ;)

Você provavelmente está pensando: Poxa, perdi isso tudo? =(

É, você perdeu isso, mas os próximos só dependem de você, esses encontros acontecerão a cada 15 dias, nas quartas-feiras às 19h. Para se increver nos próximos, basta assinar a nossa [lista de discussão](https://groups.google.com/forum/?hl=en#!forum/devopscarioca)
