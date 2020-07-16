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

import {UserInfoPanel, UserSearch, UserAvatar} from './components/profile'
import {Header} from './components/header'


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
        <Header userInfoDict={this.state.userInfoDict}/>
        <Container>
          <Row className="profileInfo">
            <Col lg="6">
              <UserInfoPanel userInfoDict={this.state.userInfoDict}/>
            </Col>
            <Col lg="4">
              <UserSearch accessToken={this.state.accessToken} onGetUserInfo={this.getUserInfo}/>
              <UserAvatar url={this.state.userInfoDict.avatar_url}/>
            </Col>
          </Row>
        </Container>
      </div>
    );
  }
}

export default App;
