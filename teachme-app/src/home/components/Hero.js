import React from 'react';
import './Hero.css';

import { Router, Link } from "@reach/router"

function Hero() {
  return (
    <section class="hero">
        <div class="cta-text">
            <h1>Venha para o Teach.me</h1>
            <p><strong>Seja um aluno e agende aulas em minutos!</strong><br/>Dê um upgrade na sua carreira aprendendo algo novo ou finalmente superando uma dificuldade.</p>
            <p><strong>Seja um instrutor e ganhe dinheiro compartilhando conhecimento.</strong><br/>Aqui suas habilidades valem muito.</p>
            <p>Quer aproveitar todas as vantagens que o Teach.me tem para oferecer? Faça já o seu cadastro.</p> 
            <p class="text-center"><Link to="/criar-conta" class="btn btn-secondary">CADASTRE-SE AGORA</Link></p>
        </div>
        <img src={process.env.PUBLIC_URL + '/images/formando.jpg'} />
    </section>
  );
}

export default Hero;