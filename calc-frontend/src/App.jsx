/**
 * Author: Bhavin Thakar
 * filename:App.jsx
 * function: react default App file
 */
import React, { useState } from "react";
import { ToastContainer } from "react-toastify";
import Calculator from "./components/Calculator";

function App() {
  return (
    <>
    <main>
      <Calculator />
    </main>
    <ToastContainer 
    position="bottom-right"
    autoClose={5000}
    hideProgressBar={true}
    newestOnTop={false}
    closeOnClick
    rtl={false}
    pauseOnFocusLoss
    draggable
    pauseOnHover
    theme="colored"
    />
    </>
    
  );
}

export default App;