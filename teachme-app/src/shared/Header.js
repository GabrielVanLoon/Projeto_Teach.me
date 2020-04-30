import React from 'react';
import './Header.css';

function Header() {
  return (
    <header id="header">
        <h2 class="logo">Teach.me</h2>
        <div class="sign-in">
            <button class="btn">Entrar</button>
            <small>Ainda não possui conta? <a href="#">Clique aqui.</a></small>
        </div>
    </header>
  );
}

export default Header;
