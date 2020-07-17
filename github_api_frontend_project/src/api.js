import config from 'react-global-configuration'


class API {
    constructor(accessToken){
        this.accessToken = accessToken;
        
        let host = config.get("BackendHost");
        this.apiUrl = host + "/api/v1";
    }

    fetchUsernameInfo = (username) => {
        var url = `${this.apiUrl}/profile/info/${username}`;
        if (!username)
          var url = `${this.apiUrl}/profile/info`;

        return this._get(url);
        
      }
    
    fetchVisibility = () => {
      let url = `${this.apiUrl}/profile/visibility`
      return this._get(url)
    }

    setVisibility = (isVisible) => {
      let url = `${this.apiUrl}/profile/visibility`

      return this._post(url, {"is_visible": isVisible})
    }

    _get = (url) => {
      console.log(url)
      return fetch(url, {
        headers: {
          Authorization: `Bearer ${this.accessToken}`
        }})
        .then(res => res.json())
        .then(
          (result) => {
            return result
          },
          (error) => {
            console.log('error', error)
          }
        )
    }

    _post = (url, data) => {
      console.log(url)
      return fetch(url, {
        method: 'POST',
        headers: {
          Authorization: `Bearer ${this.accessToken}`,
          "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
      })
        .then(res => res.json())
        .then(
          (result) => {
            return result
          },
          (error) => {
            console.log('error', error)
          }
        )
    }
}


export default API;