import React from 'react';

const NavBar = () => {

    console.log("Made it to navbar");

    return (
        <>
            <nav className="navbar navbar-expand-lg navbar-custom">
                <a className="navbar-brand" href="/index">    
                    <img src={'static/makers-logo-lockupv-black.png'} alt='makersLogo'/>
                </a>

                <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>

                <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
                    <div className="navbar-nav mr-auto"></div>

                    <div className="navbar-nav">
                        <a className="nav-item nav-link" href="/index/about">About</a>
                        <a className="nav-item nav-link" href="/login">Login</a>
                    </div>

                    <form className="form-inline my-2 my-lg-0">
                        <input className="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search"/>
                        <button className="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
                    </form>
                </div>
            </nav>
        </>
    );
};

const root = ReactDOM.createRoot(document.getElementById('navbar'));
root.render(<NavBar />);

export default NavBar;
