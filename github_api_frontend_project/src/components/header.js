import React, { Component } from 'react';

import {
    Button,
    ButtonGroup,
    Row,
    Col,
    Container,
    Card,
    Form,
    InputGroup,
    FormControl,
    Navbar,
    Nav } from 'react-bootstrap';
    

class Header extends Component {
    leftSide = () => {
      let info = this.props.userInfoDict;
  
      return [
        <Nav.Link href={info.html_url}>Home</Nav.Link>,
        <Nav.Link href={info.repos_url}>Repositories</Nav.Link>,
        <Nav.Link href={info.gists_url}>Gist</Nav.Link>,
        <Nav.Link href={info.subscriptions_url}>Subscriptions</Nav.Link>,
        <Nav.Link href={info.organizations_url}>Organizations</Nav.Link>,
      ]
    }
  
    rightSide = () => {
      let info = this.props.userInfoDict;
  
      return [
        <Nav.Link href={info.followers_url}>Followers: {info.followers}</Nav.Link>,
        <Nav.Link href={info.following_url}>Following: {info.following}</Nav.Link>,
      ]
    }
  
    render() {
      return (
        <Navbar bg="dark" variant="dark" className="header">
          <Navbar.Brand href="#home">Header</Navbar.Brand>
          <Nav className="mr-auto links">
            <div className="linksLeft">{this.leftSide()}</div>
            <div className="linksRight">{this.rightSide()}</div>
          </Nav>
        </Navbar>
      )
    }
  }

export {Header}