import React from 'react';
import './Login.css';

import { Router, Link } from "@reach/router"

function Login() {
  return (
    <main id="page-login">
        <h1>Bem vindo ao <span>Teach.me</span></h1>
        <p>Uma plataforma onde alunos e professores se encontram.</p>

        <form id="form-login">
            
            <label for="username">Nome de usuário</label>
            <input type="text" name="username"/>

            <label for='password'>Senha</label>
            <input type="password" name="password"/>

            <button type="submit" class="btn" name="btn-login">Entrar</button>
        </form>
        
        <p><small>Ainda não possui uma conta? Clique aqui e <Link to="/cadastro">cadastre-se.</Link></small></p>
    </main>
  );
}

export default Login;