/**
 * Author: Bhavin Thakar
 * filename:Calculator.jsx
 * function: file used for handling input and calling python api
 */
import React, { useState } from "react";
import axios from "axios";
import "./calculator.css";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.min.css";

export default function Calculator() {
  const [num1, setNum1] = useState("");
  const [num2, setNum2] = useState("");
  const [output, setOutput] = useState(0);
  const [loading, setLoading] = useState(false);
  const BASE_URL = import.meta.env.VITE_APP_API_BASE_URL;
  const re = /^[0-9\b]+$/;

  /**
   * clears input
   */
  function Clear() {
    setOutput(0);
    setNum1("");
    setNum2("");
  }

  /**
   * handles result for subtract
   */
  async function Subtraction() {
    let result = await getResult("sub");
    if (result.status_code == 200) {
      setOutput(result.res);
    } else {
      toast.warning(result.message);
    }
  }

  /***
   * handles result for addition
   */
  async function Addition() {
    let result = await getResult("add");
    if (result.status_code == 200) {
      setOutput(result.res);
    } else {
      toast.warning(result.message);
    }
  }
/**
 * handles input number 1 change
 * @param {*} e change event
 */
  function handleNum1Change(e) {
    setNum1(e.target.value.replace(/[^0-9.]/g, ""));
  }

  /**
   * handles input number 2 change
   */
  function handleNum2Change(e) {
    setNum2(e.target.value.replace(/[^0-9.]/g, ""));
  }

  /**
   * method for calling api
   * @param {*} routeName 
   * @returns Json Object result
   */
  async function getResult(routeName) {
    let targetUrl = `${BASE_URL}` + routeName;
    let response = {};
    response = await axios({
      method: "POST",
      url: targetUrl,
      headers: {
        "Content-Type": "application/json; charset=utf-8",
      },
      data: JSON.stringify({
        "x": Number(num1),
        "y": Number(num2),
      }),
    })
      .then((res) => res.data)
      .catch((error) => {
        toast.error(error.message);
      });
      // console.log(response);
      return response;
  }

  return (
    <>
      <h2>Calculator for Add & Subtract</h2>
      <input
        type="text"
        placeholder="Enter the number 1"
        onChange={handleNum1Change}
        value={num1}
        maxLength="8"
      />

      <input
        type="text"
        placeholder="Enter the number 2"
        onChange={handleNum2Change}
        value={num2}
        maxLength="8"
      />

      <button onClick={Addition}>Add</button>
      <button onClick={Subtraction}>Subtract</button>
      <button onClick={Clear}>Clear</button>

      <div>
        <div id="Result">
          Result : <span className="resultSpan">{output}</span>
        </div>
      </div>
    </>
  );
}
