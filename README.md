# hackathon_fase5
Hackathon do curso IA para Devs - Grupo 9

**Detecção de materiais cortantes**

  A FIAP VisionGuard, empresa de monitoramento de câmeras de
segurança, está analisando a viabilidade de uma nova funcionalidade para
otimizar o seu software.
  O objetivo da empresa é usar de novas tecnologias para identificar
situações atípicas e que possam colocar em risco a segurança de
estabelecimentos e comércios que utilizam suas câmeras.
  Um dos principais desafios da empresa é utilizar Inteligência Artificial
para identificar objetos cortantes (facas, tesouras e similares) e emitir alertas
para a central de segurança.
  A empresa tem o objetivo de validar a viabilidade dessa feature, e para
isso, será necessário fazer um MVP para detecção supervisionada desses
objetos.

**Objetivos**

- Construir ou buscar um dataset contendo imagens de facas, tesouras e
outros objetos cortantes em diferentes condições de ângulo e
iluminação;
- Anotar o dataset para treinar o modelo supervisionado, incluindo
imagens negativas (sem objetos perigosos) para reduzir falsos positivos;
- Treinar o modelo;
- Desenvolver um sistema de alertas (pode ser um e-mail).
  
**Configuração**

O arquivo "requirements.txt" estão relacionados as bibliotecas necessários para execução do projeto.
Para instalá-las execute: "pip install -r requirements.txt"

O arquivo "detect.py" contém o projeto e deverá ser executado após a instalação das bibliotecas.
