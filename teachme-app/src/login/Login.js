import React from 'react';
import API from "../utils/API";
import { useState } from "react";
import './Login.css';

import { Router, Link } from "@reach/router"

function Login() {
  
  // Os estados do componente se referem aos campos
  const [username, setUsername] = useState(""); 
  const [senha, setSenha] = useState(""); 


  const handleSubmit = (evt) => {
      evt.preventDefault();
      console.log(`Submitting Name ${username} Senha ${senha}`)

      let data = { 
        'username': username,
        'password': senha
      }

      API.get('login', data)
      .then(response => {
        console.log('SUCESSO')
        console.log(response)
      })
      .catch(error => {
          console.log('ERRO')
          console.log(error.response)
      });
  }

  return (
    <main id="page-login" class="body-card">
        <h1 class="text-center">Bem vindo ao <span id="text-name">Teach.me</span></h1>
        <p class="text-center">Uma plataforma onde alunos e professores se encontram.</p>

        <form id="form-login" onSubmit={handleSubmit} >
          <div>
            <div class="form-group">
              <label for="username">Nome de usuário</label>
              <input type="text" name="username" 
                value={username} onChange={e => setUsername(e.target.value)} />
            </div>

            <div class="form-group">
              <label for='password'>Senha</label>
              <input type="password" name="password"
                value={senha} onChange={e => setSenha(e.target.value)} />
            </div>
          </div>
          <p class="right-btn">
            <button type="submit" class="btn" name="btn-login">Entrar</button>
          </p>
        </form>
        
        <p><small>Ainda não possui uma conta? Clique aqui e <Link to="/criar-conta">cadastre-se.</Link></small></p>
    </main>
  );
}

export default Login;