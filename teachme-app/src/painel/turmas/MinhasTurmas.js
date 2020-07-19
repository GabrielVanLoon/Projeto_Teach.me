import React from 'react';
import API from "../../utils/API";
import { useState, useRef, useEffect } from "react";
import './MinhasTurmas.css';

import { Router, Link , navigate } from "@reach/router"

import CardTurma from './CardTurma'

function MinhasTurmas(props) {

    if(!localStorage.getItem('username')){
        navigate(`/login`)
    }

    const [titulo, setTitulo] = useState(''); 
    const [classname, setClassname] = useState(''); 
    const [maxParticipantes, setMaxParticipantes] = useState(10); 
    const [descricao, setDescricao]= useState(''); 


    const [status, setStatus] = useState(''); 
    const [resultados, setResultados]         = useState([]); 
    const [nroResultados, setNroResultados]   = useState(0);

    function buscarResultados(){
        let data = `username=${localStorage.getItem('username')}&situation=${status}`

        API.post('my-classes', data, { headers: { 'Content-Type': 'application/x-www-form-urlencoded' }} )
        .then(response => {
            setNroResultados(response.data.rows)
            setResultados(response.data.results)
        })
        .catch(error => {
            alert('Erro de Conexão!')
        });
    }

    useEffect(() => {
        buscarResultados()
    }, [status]);


    // handlerCadastro
    function enviarDados(){
        let data = `username=${localStorage.getItem('username')}&classname=${classname}&title=${titulo}`
        data += `&max_members=${maxParticipantes}&description=${descricao}`

        API.post('class/register', data, { headers: { 'Content-Type': 'application/x-www-form-urlencoded' }} )
        .then(response => {
            window.location.reload(false);
        })
        .catch(error => {
            alert('Ocorreu um erro ao cadastrar a turma. Tente novamente mais tarde!')
        });
    }


    const handleSubmit = async (evt) => {
        evt.preventDefault()
            
        if(!classname.match(/^[a-zA-Z0-9-_]{1,}$/)){
            alert("Classname com caractéres inválidos.")
            return false
        }

        // validando o username
        let data = `username=${classname}`
        API.post('check-username', data, { headers: { 'Content-Type': 'application/x-www-form-urlencoded' }} )
        .then(response => {
            enviarDados()
        }) 
        .catch(error => {
            alert("O classname já está em uso.")
        });
    } 

    function renderCard(item){
        return (
            <CardTurma nome={item.classname} titulo={item.title} descricao={item.description} 
                qtdMembros={item.members_quantity} maxMembros={item.max_members} situacao={item.situation} 
                ehLider={item.is_leader}/>
        )
    }

    return (
        <main id="page-minhas-turmas" class="body-card">
            <h1>Minhas Turmas</h1>

            { !props.painelInstrutor && 
                <section class="filtros">
                    <label for="filtro-status">Filtrar status </label>
                    <select id="filtro-status" name="filtro-status"
                        value={status} onChange={e => setStatus(e.target.value)}>
                        <option vaue=''>Mostrar todas</option>
                        <option value='BUSCANDO INSTRUTOR'>Buscando Instrutor</option>
                        <option value='EM AULAS'>Com aulas em curso</option>
                        <option value='ENCERRADA'>Arquivadas</option>
                    </select>
                </section> 
            }

            { props.painelInstrutor && 
                <section class="filtros">
                    <label for="filtro-status">Filtrar status </label>
                    <select id="filtro-status" name="filtro-status"
                        value={status} onChange={e => setStatus(e.target.value)}>
                        <option vaue=''>Mostrar todas</option>
                        <option value='BUSCANDO INSTRUTOR'>Buscando Instrutor</option>
                        <option value='EM AULAS'>Com aulas em curso</option>
                        <option value='ENCERRADA'>Arquivadas</option>
                    </select>
                </section> 
            }

            <section class="turmas">
                { resultados.map( renderCard ) }
            </section>

            { !props.painelInstrutor && 
                <section class="criar-turma">
                    <form onSubmit={handleSubmit}>

                        <div class="form-line">
                            <div class="form-group">
                                <label for="titulo">Título da turma</label>
                                <input type="text" id="titulo" name="titulo" minLength={2} maxLength={60} required
                                    value={titulo} onChange={e => setTitulo(e.target.value)} />    
                            </div>
                        </div>

                        <div class="form-line">
                            <div class="form-group">
                                <label for="classname">@Classname</label>
                                <input type="text" id="classname" name="classname" minLength={2} maxLength={30} required 
                                    value={classname} onChange={e => setClassname(e.target.value)}/>    
                            </div>

                            <div class="form-group">
                                <label for="max_participantes">Limite de participantes</label>
                                <input type="number" id="max_participantes" name="max_participantes"  min="2" max="30" required
                                    value={maxParticipantes} onChange={e => setMaxParticipantes(e.target.value)}/>
                            </div>
                        </div>

                        <div class="form-group">
                            <label for="descricao">Descrição da turma</label>
                            <textarea id="descricao" name="descricao" maxLength={300}
                                value={descricao} onChange={e => setDescricao(e.target.value)}></textarea>
                        </div>

                        <div class="form-group">
                            <p class="text-right"><button class="btn"><i class="fa-fw fas fa-plus"></i> Criar Nova Turma</button></p>
                        </div>
                    </form>
                </section> 
            }

        </main>
    );
  }
  
  export default MinhasTurmas;
  