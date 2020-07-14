import React, { Component } from 'react';

import queryString from 'query-string';
import ls from 'local-storage';
import config from 'react-global-configuration';

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect
} from "react-router-dom";
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

import './App.css';

import {UserInfoPanel, UserSearch} from './profile'


class LoginCallback extends Component {
  componentDidMount(){
    // fetch access and refresh tokens from url
    let parsed_qs = queryString.parse(this.props.location.search);
    this.props.onGetTokens(parsed_qs['access_token'], parsed_qs['refresh_token'])
  }

  render() {
    return  <Redirect to='/' />
  }
}


class Header extends Component {
  render() {
    return (
      <Navbar bg="dark" variant="dark">
        <Navbar.Brand href="#home">Header</Navbar.Brand>
        <Nav className="mr-auto">
          <Nav.Link href="#home">Home</Nav.Link>
          <Nav.Link href="#features">Features</Nav.Link>
        </Nav>
      </Navbar>
    )
  }
}


class App extends Component {
  state = {
    accessToken:  ls.get('accessToken') || null,
    refreshToken: null,

    userInfoDict: {}
  }

  getAuthTokens = (accessToken, refreshToken) => {
    this.setState({accessToken, refreshToken});
    ls.set('accessToken', accessToken);
  }

  getUserInfo = (userInfoDict) => {
    console.log('getuserinfo2', userInfoDict);
    this.setState({userInfoDict});
  }

  componentDidMount() {
  }

  render() {
    // If not signin on github
    if (!this.state.accessToken){
        let url = config.get('AuthURL')
        // window.location.replace(url);
        return (
          <Router>
            <h1>Please login at <a href={url}>Link</a></h1>

            <Switch>
              <Route path='/login' component={(props) => <LoginCallback {...props} onGetTokens={this.getAuthTokens} />} />
            </Switch>
          </Router>
        )
    }

    return (
      <div>
        <Header/>
        <Container>
          <Row>
            <Col lg="6">
              <UserSearch accessToken={this.state.accessToken} onGetUserInfo={this.getUserInfo}/>
            </Col>
            <Col lg="4">
              <UserInfoPanel userInfoDict={this.state.userInfoDict}/>
            </Col>
          </Row>
        </Container>
        
      </div>
    );
  }
}

export default App;
