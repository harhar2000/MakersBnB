import React from "react";
import { useNavigate } from "react-router-dom";
import { createRoot } from "react-dom-client";

const NavBar = () => {
    const navigate = useNavigate();

    const handleClick = () => {
        console.log("redirecting...");
        navigate("/about");
    };

    return (
        <nav className="navbar navbar-expand-lg navbar-custom">
        <a className="navbar-brand" onClick={handleClick}>
            <svg
            xmlns="http://www.w3.org/2000/svg"
            xmlnsXlink="http://www.w3.org/1999/xlink"
            width="260"
            height="53.945"
            viewBox="0 0 260 53.945"
            >
            <defs>
                <clipPath id="clip-path">
                <rect
                    id="Rectangle_639"
                    dataName="Rectangle 639"
                    width="260"
                    height="53.945"
                    fill="none"
                />
                </clipPath>
            </defs>
            <g
                id="Group_2591"
                dataName="Group 2591"
                transform="translate(0 0.001)"
            >
                <path
                id="Path_849"
                dataName="Path 849"
                d="M53.945,0,27.2,17.981,0,0V53.944H53.945Z"
                />
                <path
                id="Path_850"
                dataName="Path 850"
                d="M256.435,72.462l7.165-36.6L275.285,62.32l12.1-26.456,6.438,36.6h-5.269l-3.285-20.548L275.2,74.027l-9.789-22.135-3.66,20.57Z"
                transform="translate(-177.241 -24.789)"
                />
                <path
                id="Path_851"
                dataName="Path 851"
                d="M412.116,65.131H397.543L393.751,73.4h-5.534L405.061,37.22,421.309,73.4h-5.622ZM410.021,60.3l-5.048-11.574L399.681,60.3Z"
                transform="translate(-268.325 -25.726)"
                />
                <path
                id="Path_852"
                dataName="Path 852"
                d="M514.285,57.726l13.25-13.581h6.857L519,59.556,534.48,78.185H527.6L515.344,63.039,514.285,64.1V78.185h-5.137V44.145h5.137Z"
                transform="translate(-351.909 -30.512)"
                />
                <path
                id="Path_853"
                dataName="Path 853"
                d="M624.806,48.973H611.159v8.179h13.25v4.828h-13.25V73.357h13.647v4.828H606.022V44.145h18.784Z"
                transform="translate(-418.865 -30.512)"
                />
                <g id="Group_2560" dataName="Group 2560" transform="translate(0 0)">
                <g
                    id="Group_2559"
                    dataName="Group 2559"
                    clipPath="url(#clip-path)"
                >
                    <path
                    id="Path_854"
                    dataName="Path 854"
                    d="M700.221,63.678,710.76,78.185h-6.284l-9.723-13.934h-.926V78.185h-5.136V44.145h6.018q6.747,0,9.745,2.535a9.315,9.315,0,0,1,3.307,7.452,9.673,9.673,0,0,1-2.072,6.217,9.239,9.239,0,0,1-5.468,3.329m-6.394-3.9h1.632q7.3,0,7.3-5.578,0-5.225-7.1-5.225h-1.83Z"
                    transform="translate(-476.003 -30.512)"
                    />
                    <path
                    id="Path_855"
                    dataName="Path 855"
                    d="M792.159,47.736l-4.167,2.469a7.165,7.165,0,0,0-2.227-2.646,5.2,5.2,0,0,0-2.844-.705,5.253,5.253,0,0,0-3.55,1.212,3.758,3.758,0,0,0-1.411,3q0,2.492,3.7,4.013l3.4,1.389a14.493,14.493,0,0,1,6.063,4.09,9.217,9.217,0,0,1,1.918,5.92,10.4,10.4,0,0,1-3.131,7.76,10.743,10.743,0,0,1-7.826,3.087,10.469,10.469,0,0,1-7.319-2.624,12.08,12.08,0,0,1-3.55-7.386l5.2-1.146a8.846,8.846,0,0,0,1.235,4.145,5.867,5.867,0,0,0,8.621.6,5.567,5.567,0,0,0,1.587-4.078,5.723,5.723,0,0,0-.276-1.819,4.605,4.605,0,0,0-.86-1.521,6.873,6.873,0,0,0-1.51-1.3,14.584,14.584,0,0,0-2.2-1.158l-3.285-1.367q-6.989-2.954-6.989-8.643a8.2,8.2,0,0,1,2.932-6.415,10.593,10.593,0,0,1,7.3-2.6q5.887,0,9.194,5.732"
                    transform="translate(-533.041 -29.032)"
                    />
                </g>
                </g>
            </g>
            </svg>
        </a>

        <button
            className="navbar-toggler"
            type="button"
            data-toggle="collapse"
            data-target="#navbarNavAltMarkup"
            aria-controls="navbarNavAltMarkup"
            aria-expanded="false"
            aria-label="Toggle navigation"
        >
            <span className="navbar-toggler-icon"></span>
        </button>

        <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
            <div className="navbar-nav mr-auto"></div>

            <div className="navbar-nav">
            <a className="nav-item nav-link" href="/index/about">
                About
            </a>
            <a className="nav-item nav-link" href="/login">
                Login
            </a>
            </div>
            <form className="form-inline my-2 my-lg-0">
            <input
                className="form-control mr-sm-2"
                type="search"
                placeholder="Search"
                aria-label="Search"
            />
            <button
                className="btn btn-outline-success my-2 my-sm-0"
                type="submit"
            >
                Search
            </button>
            </form>
        </div>
        </nav>
    );
};

const container = document.getElementById("navbar");
const root = createRoot(container);
root.render(<NavBar />);

export default NavBar;
