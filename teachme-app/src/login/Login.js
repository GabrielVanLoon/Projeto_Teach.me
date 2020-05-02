import React from 'react';
import './Login.css';

import { Router, Link } from "@reach/router"

function Login() {
  return (
    <main id="page-login" class="body-card">
        <h1 class="text-center">Bem vindo ao <span id="text-name">Teach.me</span></h1>
        <p class="text-center">Uma plataforma onde alunos e professores se encontram.</p>

        <form id="form-login">
          <div>
            <div class="form-group">
              <label for="username">Nome de usuário</label>
              <input type="text" name="username"/>
            </div>

            <div class="form-group">
              <label for='password'>Senha</label>
              <input type="password" name="password"/>
            </div>
          </div>
          <p class="right-btn">
            <button type="submit" class="btn" name="btn-login">Entrar</button>
          </p>
        </form>
        
        <p><small>Ainda não possui uma conta? Clique aqui e <Link to="/cadastro">cadastre-se.</Link></small></p>
    </main>
  );
}

export default Login;