import React from 'react';
import API from "../utils/API";
import { useState, useRef } from "react";
import './Cadastro.css';

import { Router, Link, redirectTo} from "@reach/router"

function Cadastro() {

    // Estados: valores atuais do formulário
    const [nome, setNome]           = useState(""); 
    const [sobrenome, setSobrenome]  = useState(""); 
    const [email, setEmail]         = useState(""); 
    const [username, setUsername]   = useState(""); 
    const [senha, setSenha]         = useState(""); 
    const [repeteSenha, setRepeteSenha] = useState(""); 
    const [ehInstrutor, setEhInstrutor] = useState(false); 

    const [formacao, setFormacao] = useState(""); 
    const [resumo, setResumo] = useState(""); 

    const [cadastroRealizado, setCadastroRealizado] = useState(false);

    const emailInput    = useRef(null);
    const usernameInput = useRef(null);
    const senhaInput    = useRef(null);

    function validarCampos(){
        emailInput.current.style.borderColor = null
        usernameInput.current.style.borderColor = null
        senhaInput.current.style.borderColor = null

        if(!email.match(/^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$/)){
            alert("E-mail com formato inválido.")
            emailInput.current.focus()
            // emailInput.current.setCustomValidity("E-mail com formato inválido.");
            return false
        } 
        if(!username.match(/^[a-zA-Z0-9-_]{1,}$/)){
            alert("Username com caractéres inválidos.")
            usernameInput.current.focus()
            // usernameInput.current.setCustomValidity("Username com caractéres inválidos.");
            return false
        }
        if(senha != repeteSenha){
            alert("As senhas não coincidem.")
            senhaInput.current.focus()
            // senhaInput.current.setCustomValidity("As senhas não coincidem");
            return false
        }
        return true;
    }

    function enviarDados(){
        let data = `name=${nome}&last_name=${sobrenome}&email=${email}&username=${username}&password=${senha}`
        data += `&is_instructor=${ehInstrutor}&degree=${formacao}&abstract=${resumo}`

        API.post('register', data, { headers: { 'Content-Type': 'application/x-www-form-urlencoded' }} )
        .then(response => {
          console.log(`Olá: ${response.data.username}`)
          setCadastroRealizado(true)
        })
        .catch(error => {
            console.log(error.response)
        });
    }

    // handlerCadastro
    const handleSubmit = async (evt) => {
        evt.preventDefault()
         
        // Validação 
        if(!validarCampos())
            return;

        // validando o username
        let data = `username=${username}`
        API.post('check-username', data, { headers: { 'Content-Type': 'application/x-www-form-urlencoded' }} )
        .then(response => {
            enviarDados()
        }) 
        .catch(error => {
            alert("O username já está em uso.")
            usernameInput.current.focus()
            // usernameInput.current.setCustomValidity("O username já está em uso.");
        });
    } 

    function renderForm(){
        return (
            <main id="page-cadastro" class="body-card">
                <h1>Cadastro</h1>
                <form id="form-cadastro" onSubmit={handleSubmit}>
                    <fieldset>
                        <legend>Dados pessoais</legend>
        
                        <div class="form-group">
                            <label for="nome">Nome</label>
                            <input type="text" id="nome" name="nome"  maxLength={60} required
                                 value={nome} onChange={e => setNome(e.target.value) }/>
                        </div>
        
                        <div class="form-group">
                            <label for="sobrenome">Sobrenome</label>
                            <input type="text" id="sobrenome" name="sobrenome" maxLength={60} required
                                 value={sobrenome} onChange={e => setSobrenome(e.target.value)}/>
                        </div>
        
                    </fieldset>
                    
                    <fieldset>
                        <legend>Dados de acesso</legend>
                        
                        <div class="form-group">
                            <label for="email">E-mail</label>
                            <input type="email" id="email" name="email" maxLength={60} required
                                 ref={emailInput} value={email} onChange={e => setEmail(e.target.value)} />
                        </div>
        
                        <div class="form-group">
                            <label for="username">Nome de usuário</label>
                            <input type="text" id="username" name="username" minLength={2} maxLength={30} required
                                ref={usernameInput} value={username} onChange={e => setUsername(e.target.value)}/>
                        </div>
        
                        <div class="form-group">
                            <label for='password'>Senha</label>
                            <input type="password" id="password" name="password" minLength={8} required
                                ref={senhaInput} value={senha} onChange={e => setSenha(e.target.value)}/>
                        </div>
        
                        <div class="form-group">
                            <label for='password-repeat'>Repetir Senha</label>
                            <input type="password" id="password-repeat" name="password-repeat" minLength={8} required
                                value={repeteSenha} onChange={e => setRepeteSenha(e.target.value)}/>
                        </div>
        
                        <div>
                            <input type="checkbox" id="instrutor" name="instrutor"
                                onChange={e => setEhInstrutor(e.target.checked)}/>
                            <label for='instrutor'><small>Quero ser um instrutor Teach.me</small></label>
                        </div>
        
                        { ehInstrutor == false &&
                            <p class="btn-line">
                                {/* <button type="button" class="btn btn-inverse" name="btn-cadastro-proximo">Próximo</button> */}
                                <button type="submit" class="btn" name="btn-cadastro">Finalizar Cadastro</button>
                            </p>
                        }   
        
                    </fieldset>
                    
                    { ehInstrutor == true &&
        
                        <fieldset>
                            <legend>Dados de instrutor</legend>
        
                            <div class="form-group">
                                <label for="formacao">Formação</label>
                                <input type="text" id="formacao" name="formacao" maxLength={100} required
                                     value={formacao} onChange={e => setFormacao(e.target.value)}/>
                            </div>
        
                            <div class="form-group">
                                <label for="resumo">Resumo Sobre mim</label>
                                <textarea id="resumo" name="resumo" maxLength={300}
                                 value={resumo} onChange={e => setResumo(e.target.value)}></textarea>
                            </div>
        
                            <p class="btn-line">
                                {/* <button type="button" class="btn btn-inverse" name="btn-cadastro-voltar">Voltar</button> */}
                                <button type="submit" class="btn" name="btn-cadastro">Finalizar Cadastro</button>
                            </p>
                        </fieldset>
                    }
        
                </form>
                
            </main>
          );
    }

    function renderCadastrado(){
        return (
            <main id="page-cadastro" class="body-card">
                <h1>Cadastro Realizado!!!</h1>
                <h2>Agora você já pode desfrutar das operações do nosso aplicativo!</h2>
                <Link to="/login" className="btn" style={{ 'margin-right': '20px' }}>Fazer Login</Link>
                <Link to="/" className="btn btn-inverse">Voltar</Link>
            </main>
          );
    }

    if (cadastroRealizado){
        return renderCadastrado();
    } else {
        return renderForm();
    }
    
}

export default Cadastro;