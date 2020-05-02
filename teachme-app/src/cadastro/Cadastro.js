import React from 'react';
import './Cadastro.css';

import { Router, Link } from "@reach/router"

function Cadastro() {
  return (
    <main id="page-cadastro" class="body-card">
        <h1>Cadastro</h1>
        <form id="form-cadastro">
            <fieldset>
                <legend>Dados pessoais</legend>

                <div class="form-group">
                    <label for="nome">Nome</label>
                    <input type="text" id="nome" name="nome"/>
                </div>

                <div class="form-group">
                    <label for="sobrenome">Sobrenome</label>
                    <input type="text" id="sobrenome" name="sobrenome"/>
                </div>

                <div class="form-line">
                    <div class="form-group">
                        <label for="cidade">Cidade</label>
                        <input type="text" id="cidade" name="cidade"/>
                    </div>
            

                    <div class="form-group">
                        <label for="uf">UF</label>
                        <select id="uf" name="uf">
                            <option value="SP">São Paulo</option>
                            <option value="RJ">Rio de Janeiro</option>
                        </select>
                    </div>
                </div>

                <div class="form-group">
                    <label for='dt-nascimento'>Data de nascimento</label>
                    <input type="date" id="dt-nascimento" name="dt-nascimento"/>
                </div>

            </fieldset>
            
            <fieldset>
                <legend>Dados de acesso</legend>
                
                <div class="form-group">
                    <label for="email">E-mail</label>
                    <input type="mail" id="email" name="email"/>
                </div>

                <div class="form-group">
                    <label for="username">Nome de usuário</label>
                    <input type="text" id="username" name="username"/>
                </div>

                <div class="form-group">
                    <label for='password'>Senha</label>
                    <input type="password" id="password" name="password"/>
                </div>

                <div class="form-group">
                    <label for='password-repeat'>Repetir Senha</label>
                    <input type="password" id="password-repeat" name="password-repeat"/>
                </div>

                <div>
                    <input type="checkbox" id="instrutor" name="instrutor"/>
                    <label for='instrutor'><small>Quero ser um instrutor Teach.me</small></label>
                </div>

                <p class="btn-line">
                    <button type="button" class="btn btn-inverse" name="btn-cadastro-proximo">Próximo</button>
                    <button type="submit" class="btn" name="btn-cadastro">Finalizar Cadastro</button>
                </p>
            </fieldset>

            <fieldset>
                <legend>Dados de instrutor</legend>

                <div class="form-group">
                    <label for="formacao">Formação</label>
                    <input type="text" id="formacao" name="formacao"/>
                </div>

                <div class="form-group">
                    <label for="sobre-mim">Sobre mim</label>
                    <textarea id="sobre-mim" name="sobre-mim"></textarea>
                </div>

                <p class="btn-line">
                    <button type="button" class="btn btn-inverse" name="btn-cadastro-voltar">Voltar</button>
                    <button type="submit" class="btn" name="btn-cadastro">Finalizar Cadastro</button>
                </p>
            </fieldset>
        </form>
        
    </main>
  );
}

export default Cadastro;