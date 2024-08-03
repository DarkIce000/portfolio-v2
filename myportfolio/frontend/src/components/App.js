import React, { Component } from "react";
import { render } from "react-dom";

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
        <h1 className="bg-slate-500">Hello world</h1>
    );
  }
}

const appDiv = document.getElementById("main");
render(<App />, appDiv);