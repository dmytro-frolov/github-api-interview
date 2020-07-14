class API {
    constructor(accessToken){
        this.accessToken = accessToken;
    }

    fetchUsernameInfo = (username) => {
        var url = `http://localhost:8000/api/v1/profile/info/${username}`
        if (!username)
          var url = `http://localhost:8000/api/v1/profile/info`

        return this._fetch(url)
        
      }

    _fetch = (url) => {
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
}


export default API;