import React from 'react';
import './Menu.css';

import { Link } from "@reach/router"

function Menu(props) {

    function closeMenu(){
        props.setMenuState(false);
    }

    return (
        <React.Fragment>
            <div id="menu-sidebar" class={props.menuState && 'visible'}>
               <section class="logo">
                   <h2 class="text-center">Teach.me</h2>
               </section>

                <nav>
                    <li><Link to="/" onClick={closeMenu}><i class="fa-fw fas fa-home"/> Home</Link></li>
                </nav>

                <nav>
                    <li><Link to="instrutor" onClick={closeMenu}><i class="fa-fw fas fa-search"/> Buscar Instrutor</Link></li>
                </nav>

                <nav>
                    <li><Link to="/painel" onClick={closeMenu}><i class="fa-fw fas fa-user"/> Painel</Link></li>
                    <ul>
                        <li><Link to="/painel/minha-conta" onClick={closeMenu}>Minha Conta</Link></li>
                        <li><Link to="/painel/minhas-turmas" onClick={closeMenu}>Minhas Turmas</Link></li>
                        <li><Link to="/painel/aulas-e-propostas" onClick={closeMenu}>Aulas e Propostas</Link></li>
                    </ul>
                </nav>

                <nav>
                    <li><Link to="/painel-instrutor" onClick={closeMenu}><i class="fa-fw fas fa-graduation-cap"/> Painel Instrutor</Link></li>
                    <ul>
                        <li><Link to="/painel-instrutor/horarios-e-locais" onClick={closeMenu}>Horários e Locais</Link></li>
                        <li><Link to="/painel-instrutor/oferecimentos" onClick={closeMenu}>Meus Oferecimentos</Link></li>
                        <li><Link to="/painel-instrutor/minhas-turmas" onClick={closeMenu}>Minhas Turmas</Link></li>
                    </ul>
                </nav>
                
            </div>

            <div id="menu-shadow" class={props.menuState && 'visible'} onClick={closeMenu}>
                <button class="btn btn-inverse">Fechar Menu <i class="fa-fw fas fa-times"/> </button>    
            </div>
        </React.Fragment>
    );
}

export default Menu;