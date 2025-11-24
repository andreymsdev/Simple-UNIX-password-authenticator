# Simple UNIX password authenticator 

---

Este script Python demonstra como autenticar usuários em um sistema operacional baseado em Unix (como Linux ou macOS) verificando a senha fornecida pelo usuário contra o hash armazenado no sistema.

Este é um script educacional utilizados em CTFs. Ele acessa informações de autenticação do sistema e deve ser usado com cautela. A execução geralmente requer privilégios de `root` (usando `sudo`) se o seu sistema usa senhas shadow (`/etc/shadow`).

---

## Funcionalidades

* Solicita um nome de usuário.
* Solicita a senha de forma segura.
* Verifica o hash da senha utilizando o `passlib`.
* Informa se o login foi bem-sucedido ou não.

### Bibliotecas

```bash
pip install passlib
/caminho/para/seu/.venv/bin/python -m pip install passlib
