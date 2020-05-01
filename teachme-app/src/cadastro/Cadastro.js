import React from 'react';
import './Cadastro.css';

import { Router, Link } from "@reach/router"

function Cadastro() {
  return (
    <main id="page-cadastro">
        <h1>Cadastro</h1>
        <form id="form-cadastro">
            <fieldset>
                <legend>Dados pessoais</legend>

                <label for="nome">Nome</label>
                <input type="text" id="nome" name="nome"/>

                <label for="sobrenome">Sobrenome</label>
                <input type="text" id="sobrenome" name="sobrenome"/>

                <label for="cidade">Cidade</label>
                <input type="text" id="cidade" name="cidade"/>

                <label for="uf">uf</label>
                <select id="uf" name="uf">
                    <option value="SP">São Paulo</option>
                    <option value="RJ">Rio de Janeiro</option>
                </select>

                <label for='dt-nascimento'>Data de nascimento</label>
                <input type="date" id="dt-nascimento" name="dt-nascimento"/>

            </fieldset>
            
            <fieldset>
                <legend>Dados de acesso</legend>
                
                <label for="email">E-mail</label>
                <input type="mail" id="email" name="email"/>

                <label for="username">Nome de usuário</label>
                <input type="text" id="username" name="username"/>

                <label for='password'>Senha</label>
                <input type="password" id="password" name="password"/>

                <label for='password-repeat'>Repetir Senha</label>
                <input type="password" id="password-repeat" name="password-repeat"/>

                <input type="checkbox" id="instrutor" name="instrutor"/>
                <label for='instrutor'><small>Quero ser um instrutor Teach.me</small></label>

                <button type="button" class="btn" name="btn-cadastro-proximo">Próximo</button>
                <button type="submit" class="btn" name="btn-cadastro">Finalizar Cadastro</button>
            </fieldset>

            <fieldset>
                <legend>Dados de instrutor</legend>

                <label for="formacao">Formação</label>
                <input type="text" id="formacao" name="formacao"/>

                <label for="sobre-mim">Sobre mim</label>
                <textarea id="sobre-mim" name="sobre-mim"></textarea>

                <button type="button" class="btn" name="btn-cadastro-voltar">Voltar</button>
                <button type="submit" class="btn" name="btn-cadastro">Finalizar Cadastro</button>
            </fieldset>
        </form>
        
    </main>
  );
}

export default Cadastro;