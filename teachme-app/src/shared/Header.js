import React from 'react';
import './Header.css';

import { Router, Link } from "@reach/router"

function Header(props) {

  function toggleMenu(){
    props.setMenuState(true)
  }
  
  return (
    <header id="header">
      <div class="logo">
        <button id="btn-menu" onClick={ toggleMenu }><i class="fa-fw fas fa-bars"/></button>
        <h2><Link to="/">Teach.me</Link></h2>
      </div>
      <div class="sign-in">
          <Link to="/login" className="btn">Entrar</Link>
          <small>Ainda não possui conta? <Link to="/criar-conta">Clique aqui. </Link></small>
          <small> Usuario atual: { localStorage.getItem('username') || 'Nenhum '}</small>
      </div>
    </header>
  );
}

export default Header;
