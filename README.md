<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



<h3 align="center">CivitAI Downloader</h3>

  <p align="center">
    This project uses the CivitAI REST API to find, extract, and download all files created by a specific user.
    <br />
    <a href="https://github.com/UniversaParadox/CivitAI_Downloader"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/UniversaParadox/CivitAI_Downloader">View Demo</a>
    ·
    <a href="https://github.com/UniversaParadox/CivitAI_Downloader/issues">Report Bug</a>
    ·
    <a href="https://github.com/UniversaParadox/CivitAI_Downloader/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#What-does-this-do?">What does this do?</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Small project that I made for a friend to easily download CivitAI models from one creator.


Files within this repository

.wget-hsts - Protection with using wget

COPYING.txt - GNU3 License Copy

LICENSE - GNU3 License

README.md - This file

Run.bat - Simple windows batch file to run the script.

civitai.py - Script itself

wget.ext - https://www.gnu.org/software/wget/

previous_directory.txt - Contains the default path where the creator folder will be stored and created. If nothing is given, script directory will be used instead.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started



### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Python
  ```sh
  https://www.python.org/
  ```
* Pandas
  ```sh
  pip install pandas
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/UniversaParadox/CivitAI_Downloader.git
   ```
2. Run 'Run.bat'

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## What does this do?

This project uses the CivitAI REST API to find, extract, and download all files created by a specific user. To be more specific, this files does the following.

User inputs the creator's username. Script then searches for the user in CivitAI and will confirm/deny if the user exists. If the user does not exist, it will ask for you to try again. If the user does exist, it will then use the civitAI API to query and then extract information to push to a CSV file. Once the information is extracted and parsed, it will find download URL for the files and begin to download them. In order to make sure all downloads are done without isssue, there is a baked in 3 second wait period between downloads.

Below is the information stored into the CSV file.

Name

Type of File

Description

API download link

Trigger Words (if LORA file)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

TBD

See the [open issues](https://github.com/UniversaParadox/CivitAI_Downloader/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GNU3 License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact


Project Link: [https://github.com/UniversaParadox/CivitAI_Downloader](https://github.com/UniversaParadox/CivitAI_Downloader)

<p align="right">(<a href="#readme-top">back to top</a>)</p>





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/UniversaParadox/CivitAI_Downloader.svg?style=for-the-badge
[contributors-url]: https://github.com/UniversaParadox/CivitAI_Downloader/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/UniversaParadox/CivitAI_Downloader.svg?style=for-the-badge
[forks-url]: https://github.com/UniversaParadox/CivitAI_Downloader/network/members
[stars-shield]: https://img.shields.io/github/stars/UniversaParadox/CivitAI_Downloader.svg?style=for-the-badge
[stars-url]: https://github.com/UniversaParadox/CivitAI_Downloader/stargazers
[issues-shield]: https://img.shields.io/github/issues/UniversaParadox/CivitAI_Downloader.svg?style=for-the-badge
[issues-url]: https://github.com/UniversaParadox/CivitAI_Downloader/issues
[license-shield]: https://img.shields.io/github/license/UniversaParadox/CivitAI_Downloader.svg?style=for-the-badge
[license-url]: https://github.com/UniversaParadox/CivitAI_Downloader/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
