// index.js
import React from "react";
import NavBar from "./frontend/src/components/navBar.jsx"; // Import your React component
import { createRoot } from "react-dom-client";

const container = document.getElementById("navbar");

const root = createRoot(container);
root.render(<NavBar />);
