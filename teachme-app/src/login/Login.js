import React from 'react';
import API from "../utils/API";
import { useState, useRef } from "react";
import './Login.css';

import { Router, Link, navigate } from "@reach/router"

function Login() {
  
  // Os estados do componente se referem aos campos
  const [username, setUsername] = useState(""); 
  const [senha, setSenha] = useState(""); 
  const [loginIncorreto, setLoginIncorreto] = useState(false); 

  const usernameInput = useRef(null);
  const senhaInput    = useRef(null);


  function validarCampos(){
    usernameInput.current.style.borderColor = null

    if(!username.match(/^[a-zA-Z0-9-_]{1,}$/)){
      alert("Username com caractéres inválidos.")
      usernameInput.current.focus()
      return false
    } 

    return true;
  }

  function enviarDados(){
    let data = `username=${username}&password=${senha}`

    API.post('login', data, { headers: { 'Content-Type': 'application/x-www-form-urlencoded' }} )
    .then(response => {
      localStorage.setItem('username', response.data.username)
      localStorage.setItem('name',     response.data.name)
      localStorage.setItem('last_name', response.data.last_name)
      localStorage.setItem('email', response.data.email)
      localStorage.setItem('is_instructor', response.data.is_instructor)
      // navigate(`/painel`)
      window.location.reload(false);
    })
    .catch(error => {
      usernameInput.current.focus()
      setLoginIncorreto(true)
    });
  }

  const handleSubmit = async (evt) => {
    evt.preventDefault()
     
    // Validação 
    if(!validarCampos())
        return;

    // Enviando os dados
    enviarDados()
} 

  return (
    <main id="page-login" class="body-card">
        <h1 class="text-center">Bem vindo ao <span id="text-name">Teach.me</span></h1>
        <p class="text-center">Uma plataforma onde alunos e professores se encontram.</p>

        <form id="form-login" onSubmit={handleSubmit} >
          <div>
            <div class="form-group">
              <label for="username">Nome de usuário</label>
              <input type="text" name="username" minLength={2} maxLength={30} required
                ref={usernameInput} value={username} onChange={e => setUsername(e.target.value)} />
            </div>

            <div class="form-group">
              <label for='password'>Senha</label>
              <input type="password" name="password" minLength={8} required
                ref={senhaInput} value={senha} onChange={e => setSenha(e.target.value)} />
            </div>
          </div>
          <p class="right-btn">
            { loginIncorreto && 
              <span for="username" style={{'color': 'red', 'margin-right': '10px'}}>Usuário ou Senha inválidos.</span>
            }
            <button type="submit" class="btn" name="btn-login">Entrar</button>
          </p>
         
        </form>
        
        <p><small>Ainda não possui uma conta? Clique aqui e <Link to="/criar-conta">cadastre-se.</Link></small></p>
    </main>
  );
}

export default Login;