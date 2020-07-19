import React from 'react';
import API from "../../utils/API";
import { useState, useRef, useEffect } from "react";
import './MeuPerfil.css';

import { Router, Link, navigate } from "@reach/router"

function MeuPerfil() {
  
    if(!localStorage.getItem('username')){
        navigate(`/login`)
    }

    const [nome, setNome]           = useState(localStorage.getItem('name')); 
    const [sobrenome, setSobrenome]  = useState(localStorage.getItem('last_name')); 
    const [email, setEmail]         = useState(localStorage.getItem('email')); 
    const [username, setUsername]   = useState(localStorage.getItem('username'));  
    const [ehInstrutor, setEhInstrutor] = useState(localStorage.getItem('is_instructor')); 

  // handlerCadastro
  const handleSubmit = async (evt) => {
      evt.preventDefault()

      // validando o username
      let data = `name=${nome}&last_name=${sobrenome}&username=${username}`
      API.post('user/update', data, { headers: { 'Content-Type': 'application/x-www-form-urlencoded' }} )
      .then(response => {
        localStorage.setItem('name',     response.data.name)
        localStorage.setItem('last_name', response.data.last_name)
        window.location.reload(false);
      }) 
      .catch(error => {
          alert("Ocorreu um erro. Tente novamente mais tarde!")
      });
  } 

  return (

    <main id="page-meu-perfil" class="body-card">
      <h1>Meu Perfil</h1>
      <form id="form-cadastro" onSubmit={handleSubmit}>
          
          <fieldset>
              <legend>Dados pessoais</legend>

              <div class="form-group">
                  <label for="email">E-mail</label>
                  <input type="email" id="email" name="email" maxLength={60} required
                     value={email} disabled/>
              </div>

              <div class="form-group">
                  <label for="username">Nome de usuário</label>
                  <input type="text" id="username" name="username" minLength={2} maxLength={30} required
                     value={username} disabled />
              </div>
 
              <div class="form-group">
                  <label for="nome">Nome</label>
                  <input type="text" id="nome" name="nome"  maxLength={60} required
                      value={nome} onChange={e => setNome(e.target.value)}/>
              </div>

              <div class="form-group">
                  <label for="sobrenome">Sobrenome</label>
                  <input type="text" id="sobrenome" name="sobrenome" maxLength={60} required
                      value={sobrenome} onChange={e => setSobrenome(e.target.value)}/>
              </div>
              <div class="form-group">
                <p class="btn-line">
                    <button type="submit" class="btn" name="btn-cadastro">Atualizar Dados</button>
                </p>
              </div>
          </fieldset>

      </form>
      
  </main>
  );
}

export default MeuPerfil;