import React, { Component } from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect
} from "react-router-dom";

import queryString from 'query-string';
import ls from 'local-storage'
import config from 'react-global-configuration'

import { Button, ButtonGroup, Row, Col, Container, Card, Form } from 'react-bootstrap';
import './App.css';


class UserSearch extends Component {
  state = {
    username: "",
    isLoading: false
}

  fetchUsernameInfo = (username) => {
    let url = `http://localhost:8000/api/v1/profile/info/${username}`

    fetch(url)
      .then(res => res.json())
      .then(
        (result) => {
          console.log(result);

          this.setState({
            isLoaded: true,
            items: result.items
          });
        },
        (error) => {
          this.setState({
            isLoaded: true,
            error
          });
        }
      )
  
  }

  changeUsernameHandler = (e) => {
    let username = e.target.value;
    this.fetchUsernameInfo(username);
  }

  render() {
    return <Form>
      <Form.Group controlId="formSearchUser">
        <Form.Label>Username</Form.Label>
        <Form.Control type="input" placeholder="Enter username" onChange={this.changeUsernameHandler} />
      </Form.Group>
    </Form>
  };
}


class UserInfoPanel extends Component {
  render() {
    return <div></div>
  }
}


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
    refreshToken: null
  }

  getAuthTokens = (accessToken, refreshToken) => {
    this.setState({accessToken, refreshToken});
    ls.set('accessToken', accessToken)
  }

  componentDidMount() {
  }

  render() {
    // If not signin on github
    if (!this.state.accessToken){
        let url = config.get('AuthURL')
        // window.location.replace(url);
        return <h1>Please login at <a href={url}>Link</a></h1>
    }

    return (
      <Router>
      <div>
        <Row>
          <Col lg="6">
            <UserSearch>
            </UserSearch>
          </Col>
          <Col lg="4">
            space

          </Col>

        </Row>

      </div>
      <div>

        <Switch>
          <Route path='/login' component={(props) => <LoginCallback {...props} onGetTokens={this.getAuthTokens} />} />
        </Switch>
      </div>
    </Router>


    );
  }
}

export default App;
