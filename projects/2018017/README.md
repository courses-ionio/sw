<h2 align="center">Software Engineering</h2>

<h3 align="center">Vasileios Provopoulos | ID/RN: P2018017 | <a href="mailto:p18prov@ionio.gr">p18prov@ionio.gr</a></h3>

### Table of Contents

| Week | Deliverable(s) |
| --- | --- |
| 1st | [Introduction](#Introduction) |
| 2nd | [CV](#Curriculum-Vitae) |
| 3rd | [Pull request @ CSCW website/other project](#Collaborative-DEV)  |
| 4th | [Command-line exercise](#Command-line-exercises) |
| 5th | [Participatory content](#Participatory-Content) |
| 6th | [Command-line exercise](#Command-line-exercises) |
| 7th | [CV](#Curriculum-Vitae) |
| 8th | Pull request @ CSCW website/other project |
| 9th | [Command-line exercise](#Command-line-exercises) |
| 10th | [Participatory content](#Participatory-Content) |
| 11th | [Command-line exercise](#Command-line-exercises) |
| 12th | [Conclusion](#Conclusion) |

### Introduction
Software engineering should be at the forefront of everything that involves computer science concepts for the development and maintenance of dependable software. It is self evident that software development is a very intricate process, especially so in real-world applications that are large and complicated. Thus, in order to produce reliable, efficient and scalable software, the understanding of software engineering concepts and principles **_is required in parallel_** with software development. There is a wide range of fields included in SE, such as lifecycle models, software requirements, validation and verification, development environments, quality assurance design and project management among others.
<br>
The primary focus of this course will be laid on development environments, continuous integration, software automation and performance measurement while other fields may be sequentially covered on a case-by-case basis.<br>
In that regard, some personal pursuits are set:
* Experiment with a different toolchain set (OS, compilers, debuggers etc.)
* Employ the right combination of methodologies, tools and procedures to support safe, reliable and efficient human-centered design in a selected software environment
* Enhance workflow productivity with DE setup automation

### Weekly Video Quizzes
Answers to the weekly quizzes can be found at [this](https://github.com/provopoulos/sw/blob/quizzes-2018017/projects/2018017/README.md) external report.
### Curriculum Vitae
<p>
  <a href="https://provopoulos.github.io/swcv/" title="Vasileios Provopoulos">
    <img src="https://github.com/provopoulos/sw/blob/quizzes-2018017/projects/2018017/images/curriculum-vitae.png" alt="[CV]: VP"/>
  </a>
</p>

<p align="center"><em>Click on picture to view CV online</em> | <a href="https://provopoulos.github.io/swcv/"><em>fallback</em></a></p>
<p align="center"><em>Repository: </em><a href="https://github.com/provopoulos/swcv"><em>p18prov/swcv</em></a></p>
<p align="center"><em>Workflow Event (Github Action): </em><a href="https://github.com/provopoulos/swcv/blob/development/.github/workflows/continuous-integration.yml"><em>continuous-integration.yml</em></a></p>

A minimalist curriculum vitae written in HTML & CSS which is hosted online by Github Pages. The actual data (contact details, projects, skills etc.) are stored in a human-readable data-serialization [configuration file](https://github.com/provopoulos/swcv/blob/development/_data/details.yml) that HTML reads off of it at build time. This compartmentalized structure proved rather useful because it paired up well with support for [PDF automatic generation](https://github.com/provopoulos/swcv/blob/gh-pages/output/) which was introduced at a later time.

The most prominent characteristic of this PDF automatic generation is that it **only** gets triggered once the above-mentioned configuration file gets amended. That creates less overhead in situations where other files need to updated as the [workflow event](https://github.com/provopoulos/swcv/actions/workflows/continuous-integration.yml) won't be activated in these cases.

Local setup & push to Github record is on [Asciinema](https://asciinema.org/a/SQxqbgae56nYsZAvxtEDeovRX).<br>
Initial support for PDF, commit: [provopoulos/swcv@54370ec](https://github.com/provopoulos/swcv/commit/54370ec9f1270131191a5df1443295f854c5a5d5).<br>

### Collaborative-DEV
#### [#MINIMAL-IONIO](https://github.com/ioniodi/minimal-ionio), [#SITEGR](https://github.com/ioniodi/sitegr)
| Issue                                              	| PR                                                   	| Demo                                                                  	| Branch(es)                                                                                                                	|
|----------------------------------------------------	|------------------------------------------------------	|-----------------------------------------------------------------------	|---------------------------------------------------------------------------------------------------------------------------	|
| [#61](https://github.com/ioniodi/sitegr/issues/61) 	| SG: [#91](https://github.com/ioniodi/sitegr/pull/91) 	| [Timetable](https://tender-shaw-215180.netlify.app/timetables/sem_8/) 	| [provopoulos/sitegr@sem8_2021](https://github.com/provopoulos/sitegr/blob/sem8_2021/all_collections/_timetables/sem_8.md) 	|
### Issues and PRs
|                          Feedback                         |                                                                                                                                                                   Issues                                                                                                                                                                  |                                                                                                                                                                         PRs                                                                                                                                                                        |
|:---------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|        [sitegr](https://github.com/ioniodi/sitegr)        | [Commented by me](https://github.com/ioniodi/sitegr/issues?q=is%3Aissue+commenter%3Aprovopoulos+is%3Aclosed)<br> [Assigned to me](https://github.com/ioniodi/sitegr/issues?q=is%3Aissue+assignee%3Aprovopoulos+is%3Aclosed)<br> [Mentioning me](https://github.com/ioniodi/sitegr/issues?q=is%3Aissue+mentions%3Aprovopoulos+is%3Aclosed) |            **[Commented by me](https://github.com/ioniodi/sitegr/pulls?q=is%3Apr+commenter%3Aprovopoulos+is%3Aclosed)**<br> [Assigned to me](https://github.com/ioniodi/sitegr/pulls?q=is%3Apr+assignee%3Aprovopoulos+is%3Aclosed)<br> [Mentioning me](https://github.com/ioniodi/sitegr/pulls?q=is%3Apr+mentions%3Aprovopoulos+is%3Aclosed)           |
| [minimal-ionio](https://github.com/ioniodi/minimal-ionio) |                                                                                                                                                                     -                                                                                                                                                                     | [Commented by me](https://github.com/ioniodi/minimal-ionio/pulls?q=is%3Apr+commenter%3Aprovopoulos+is%3Aclosed)<br> [Assigned to me](https://github.com/ioniodi/minimal-ionio/pulls?q=is%3Apr+assignee%3Aprovopoulos+is%3Aclosed)<br> [Mentioning me](https://github.com/ioniodi/minimal-ionio/pulls?q=is%3Apr+mentions%3Aprovopoulos+is%3Aclosed) |

### Command-line exercises
#### [#Software](https://github.com/epidrome/dokey#software)
|                 Task                |                                                            Deliverables                                                            |                               Actions                               |  Commit  |
|:----------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------:|:--------:|
| Test an alternative stack of tools | Set-up an OS image with a set of CLI tools with minimal dependencies and a software license that allows commercial use and selling | [<img src="https://asciinema.org/a/MMCLu0FldyKMhUmZ1IGNy11ZB.svg" width="100">](https://asciinema.org/a/MMCLu0FldyKMhUmZ1IGNy11ZB) | &#x2611; |
| Set-up continuous integration | Build and deploy your CV dynamically every time you make a small change in the source files | [Deployments](https://github.com/provopoulos/swcv/actions/workflows/continuous-integration.yml)<br>[swcv](https://github.com/provopoulos/swcv/blob/development/.github/workflows/continuous-integration.yml)| &#x2611; |
| Performance monitoring | Monitor the performance of your Python scripts and visualize them with colors and spark lines | [<img src="https://asciinema.org/a/ClUPgjuCvXOVC0dXWuEIx7Ddv.svg" width="100">](https://asciinema.org/a/ClUPgjuCvXOVC0dXWuEIx7Ddv)| &#x2611; |
| Create an agent for news | The demo should display the new content added on a news website | [<img src="https://asciinema.org/a/Y8jdT5HO9BbAjfSCw0Z934tTb.svg" width="100">](https://asciinema.org/a/Y8jdT5HO9BbAjfSCw0Z934tTb)| &#x2611; |

### Participatory Content

2018017-pt1: [[site]](https://github.com/provopoulos/site/tree/2018017-pt1) | [[_gallery]](https://github.com/provopoulos/_gallery/tree/2018017-pt1) | [[images]](https://github.com/provopoulos/images/tree/2018017-pt1)<br>
2018017-pt2: [[site]](https://github.com/provopoulos/site/tree/2018017-pt2) | [[_gallery]](https://github.com/provopoulos/_gallery/tree/2018017-pt2) | [[images]](https://github.com/provopoulos/images/tree/2018017-pt2) | [[extras]](https://github.com/provopoulos/extras/tree/2018017-pt2)

| Additions @ pibook |                                                                                                                                                                                  Repositories                                                                                                                                                                                 |                                                                                                                                                                                                                Netlify                                                                                                                                                                                                                |                                          Setup                                          |
|:------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|
|       Matlab       |     [provopoulos/images/matlab.jpg](https://github.com/provopoulos/images/blob/61c3df1c54ccedda7dbcce7a195d22555ebfb147/matlab.jpg)<br> [provopoulos/_gallery/matlab.md](https://github.com/provopoulos/_gallery/blob/fc04c3a489b00abf341ee83e6120fc4febc401c7/matlab.md)<br> [provopoulos/site@2018017-pt1](https://github.com/provopoulos/site/commits/2018017-pt1)<br>     |                                                                                          [gallery/matlab](https://eager-raman-999e49.netlify.app/gallery/matlab/)<br> [slides/tools](https://eager-raman-999e49.netlify.app/slides/tools/)<br> [timeline/programming@1979](https://eager-raman-999e49.netlify.app/timeline/programming/)<br>                                                                                          |           [<img src="https://asciinema.org/a/4koQJ4dmoixO4aOlHhSbjHbuG.svg" width="100">](https://asciinema.org/a/4koQJ4dmoixO4aOlHhSbjHbuG)           |
|      NeXTSTEP      | [provopoulos/images/nextstep.jpg](https://github.com/provopoulos/images/blob/61c3df1c54ccedda7dbcce7a195d22555ebfb147/nextstep.jpg)<br> [provopoulos/_gallery/nextstep.md](https://github.com/provopoulos/_gallery/blob/fc04c3a489b00abf341ee83e6120fc4febc401c7/nextstep.md)<br> [provopoulos/site@2018017-pt1](https://github.com/provopoulos/site/commits/2018017-pt1)<br> | [gallery/nextstep](https://eager-raman-999e49.netlify.app/gallery/nextstep/)<br> [slides/method](https://eager-raman-999e49.netlify.app/slides/method/)<br> [timeline/multimedia@1989](https://eager-raman-999e49.netlify.app/timeline/multimedia/)<br> [timeline/personal@1989](https://eager-raman-999e49.netlify.app/timeline/personal/)<br> [timeline/systems@1989](https://eager-raman-999e49.netlify.app/timeline/systems/)<br> | [<img src="https://asciinema.org/a/4koQJ4dmoixO4aOlHhSbjHbuG.svg" width="100">](https://asciinema.org/a/4koQJ4dmoixO4aOlHhSbjHbuG) |
|      Tim Berners-Lee      | [provopoulos/images/tim-bl.jpg](https://github.com/provopoulos/images/blob/8dfbf6c5bee67b5e855626dc192a2d5821173747/tim-bl.jpg)<br> [provopoulos/extras/bio-timbl.md](https://github.com/provopoulos/extras/blob/a33e05439b31ca15b0f41641e5ca82755f080b6d/bio-timbl.md)<br> [provopoulos/site/_biography/tim-bl.md](https://github.com/provopoulos/site/blob/2018017-pt2/_biography/tim-bl.md)<br> [provopoulos/site@2018017-pt2](https://github.com/provopoulos/site/commits/2018017-pt2)<br> | [biography/](https://nostalgic-kare-0a0074.netlify.app/biography/)<br> [biography/tim-bl/](https://nostalgic-kare-0a0074.netlify.app/biography/tim-bl/)<br> | [<img src="https://asciinema.org/a/4koQJ4dmoixO4aOlHhSbjHbuG.svg" width="100">](https://asciinema.org/a/4koQJ4dmoixO4aOlHhSbjHbuG) |
|      Objective-C      | [provopoulos/images/objc.jpg](https://github.com/provopoulos/images/blob/8dfbf6c5bee67b5e855626dc192a2d5821173747/objc.jpg)<br> [provopoulos/extras/cs-objc.md](https://github.com/provopoulos/extras/blob/a33e05439b31ca15b0f41641e5ca82755f080b6d/cs-objc.md)<br> [provopoulos/site/_case-study/objc.md](https://github.com/provopoulos/site/blob/2018017-pt2/_case-study/objc.md)<br> [provopoulos/site@2018017-pt2](https://github.com/provopoulos/site/commits/2018017-pt2)<br> | [case-study/](https://nostalgic-kare-0a0074.netlify.app/case-study/)<br> [case-study/objc/](https://nostalgic-kare-0a0074.netlify.app/case-study/objc/)<br> | [<img src="https://asciinema.org/a/4koQJ4dmoixO4aOlHhSbjHbuG.svg" width="100">](https://asciinema.org/a/4koQJ4dmoixO4aOlHhSbjHbuG) |

### Conclusion
Software Engineering is an intricate process if one takes into account the required steps that are involved for the development of reliable, efficient and scalable software. The historical look at the early technologies and practices is beneficial in understanding how those have reshaped the modern software as well as which of these really stood the test of time.

After completing this course, I enriched my knowledge of Git by exploring and implementing advanced functionality such as the submodules tools. As far as continuous integration is concerned, I got a basic level of understanding from automating the process of document generation each time a variable factor gets amended (in that case, CV details). This has inspired me to look into other ways of systematizing procedures such as writing up scripts that automate the process of compiling applications from source code that aren't directly available to my Linux distribution of choice but have overall support for the Linux ecosystem.
Finally, I got to work on a different operating environment (FreeBSD) which is more aligned to the Unix philosophy and thus required more configuring than the average Linux environment which is pre-configured with user-friendly defaults out of the box.

### Sources
* [The Deep History of Your Apps: Steve Jobs, NeXTSTEP, and Early Object-Oriented Programming](https://computerhistory.org/blog/the-deep-history-of-your-apps-steve-jobs-nextstep-and-early-object-oriented-programming/)
* [Inventor of World Wide Web Receives ACM A.M. Turing Award](https://awards.acm.org/about/2016-turing)
* [Tim Berners-Lee](https://www.sansimera.gr/biographies/2340)
* Official documentation for each command-line tool used (i.e. https://github.com/tomschwarz/neix#clipboard-usage : neix)
* Numerous threads/posts on Reddit and Stackoverflow for issues occurred throughout the duration of the course
