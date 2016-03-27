---
layout: post
title: For Starts
category : Common
tags : [Test, Common]
---

这是一个中文实验。
This is a test for English.

我是一枚Java攻城狮，工作两年多，主要做Java Web开发，期间转去做了一年多的[Oracle DBA](http://dylanninin.com/blog/2013/10/26/oracle_dba.html)，维护[Oracle EBS](http://dylanninin.com/blog/2013/10/25/oracle_ebs.html)，也当过[Linux Administrator](http://dylanninin.com/blog/2013/10/25/linux.html)。

Sun早就被Oracle收购了，Java和MySQL成了Oracle的小儿子；Oracle Database和EBS自不必说，Oracle的亲亲亲生孩子，庞然大物，组件众多；Oracle推出了基于Redhat的Oracle Linux，
号称Unbreakable，所以Linux Administrator就成了Oracle Linux Administrator。看这趋势，一路朝Oracle走来一路坑，深有被Oracle绑架的感觉，所以希望能够从Oracle中解脱出来，呼吸下
新鲜空气。

最近王垠新写了一篇博文[再见Voxer，你好Sourcegraph](http://www.yinwang.org/blog-cn/2013/11/08/voxer-sg)，讲述他最近的一段经历和想法，顺便小议了下Oracle：“想当年 Oracle 的那些烂东西也是用同样的方式发家的吧”。
这是不是在黑Oracle，我想不是的。在公司刚结束的一个由华南地区Oracle ACS的team主导的Oracle EBS升级项目中，有一位技术深厚、经验丰富的顾问（专攻Oracle Database，经历过8i, 9i, 10g, 11g，现在12c开始着火了）半开玩笑的说道：Oracle Database就是一堆Patch堆积起
来的。这是在食堂排队前的一点闲谈，但不无道理，以不才一年之误尚不足以体会这么深，可顾问该是有些说服力的。

甲骨文叫Oracle，而不取类似“Apache”的名字，是不是很神秘？即使这样，公司每年还是要签Oracle的License，为Oracle测试、提Bug。

在做Oracle DBA时看了阮一峰的[Java语言学校的危险性(译文)](http://www.ruanyifeng.com/blog/2008/12/the_perils_of_javaschools.html)，似乎识迷途其未远；偶尔碰见[Lisp的永恒之道](http://coolshell.cn/articles/7526.html)，编程语言真的会影响人的思维方式；昨天还看了下Hacker News上的提问[Ask HN: Is Java still worth learning?](https://news.ycombinator.com/item?id=6706402)又验证了
某些想法。现在开始觉得是时候换种语言了，在同学、朋友的影响与帮助下，开始了[RoR](http://rubyonrails.org/)之旅。

---

##Java

先简单总结下个人Java Web开发的经历。基本有三个阶段：

* 四叶草网上书店：大二数据库课程设计的项目，用到的技术很基础，JSP, Servlet, JavaBean, 数据库为MySQL。 现在早已不知道代码在哪里，好在当时开了新浪博客[四叶草团队](http://blog.sina.com.cn/s/blog_604d17d30100e0qn.html)，还留有一些可寻的印象，现在看过去文字好生硬。
* 俱乐部会员管理系统：一个暑期的项目，应该是大二结束后的暑假，由IBM教育学院派人进行培训，为其40天。从这起就是开始接触 Java Web开发框架(Struts2, Hibernate, Spring，合称SSH)；那时啥也不知道，学会了一点SSH的使用技巧后，就开始抛弃纯JSP, Servlet, JavaBean的开发了。
* 生活信息分享系统：大四毕业答辩的项目，分微博(集成新浪微博)、房产(模仿搜房)、景点(不记得模仿哪个系统了)和天气预报(集成雅虎天气)四大子系统， 因为那时LBS渐热，所以这些模块都要结合Google Maps，根据我们的想法就把它们硬生生地扯在一起了。技术框架自然是SSH，但需要整合的第三方系统实在太多， 新浪微博(OAuth和开放API)，雅虎天气(Web Service，XML或JSON)，还有Google Maps(开放API)；因为种种原因，系统完成得并不理想，庆幸的是并没有影响大家正常毕业。

工作中接触的Java Web项目，都是采用SSH的基础框架。偶尔还有点变化，前端从Adobe Flex到Ext JS3，Java FX也曾一度惊现，但缺少纯HTML和JavaScript；开始集成Lucene做简单的站内搜索， 或者干脆使用Solr；最近又要集成IM，做基于Openfire、Spark、FastPath的开发；用够了Hibernate，终于开始调研MyBatis；听说PHP和Java可以强强联合，所以又开始尝试Quercus及php-java的桥接... ...

以个人有限的知识和经历，我认为对中小型企业来说SSH框架已经基本够用。作为补充，上个月整理了一份[Java Resource](http://dylanninin.com/blog/2013/10/09/java_resource.html)可供参考。

---

##Rails

以上是从大学到工作至今接触过的一些Java Web开发的技术或框架，它们堆积在一起很吓人，说不上完全掌握，但理解还是有一点的；要说是啃老族，那我啃的还是大学的底，只是不再认为“Java Web == SSH”。

在回头审视这些项目或阅读源代码时，我有经历过一些想法的摩擦和碰撞，而这些想法又体现在Rails中，但Rails做得很好，也很优雅，当之无愧的"魔幻"。

看Rails的第一本书是[Agile Web Development with Rails 4](http://book.douban.com/subject/24718727/)，它除了教你如何认识和使用Rails，也讲了敏捷开发的流程，不得不说让人感受和启发良多。如果要说一句话，我想那会是相见恨晚。


##Java vs Rails

下文将说说这几天学Rails时脑海中时而涌现的念头，作为对Java Web开发的一次小结，也算是对Rails的一种拥抱。

这些想法很基础，可以说任何一个项目都会遇到；但也很重要，我认为只有理解和解决了它们，一个项目的基石才是可靠的。

主要包括：

* 项目结构：Top directory and packages in Java, Rails and Django;
* 命名规范：Naming Conversion; NamingStrategy in Hibernate and why plurals for tables in Rails;
* 日志处理：Log4j in Java and Logger in Rails
* 单元测试：jUnit, DbUnit in Java and Fixtures in Rails
* 构建工具：Ant in Java and Rake in Rails

特别说明：

* 在[Ask HN: Is Java still worth learning?](https://news.ycombinator.com/item?id=6706402)中看到基于Java和Scala的框架[Play Framework](http://www.playframework.com/)，对以上问题似乎解决得也很不错，具体如何，需要试用、[与Rails对比](http://vschart.com/compare/play-framework/vs/ruby-on-rails)才知道；
* 为方便引用，Agile Web Development with Rails 4以下简称AWDR4；
* 因为啃老，下文可能停留在“Java Web == SSH”的水平，欢迎拍砖和评论；
* 个人知识水平有限，若有错误还请大侠们不吝赐教；

---

##项目结构

###目录结构

####Java

Java Web应用并没有明确规定该采用怎样的目录结构，唯一可寻的规范似乎是[WAR file format](http://en.wikipedia.org/wiki/WAR_%28Sun_file_format%29)中提及的[web.xml](http://en.wikipedia.org/wiki/Web.xml)， 其中web.xml的具体内容又由[web-app_2_5](http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd)进行定义。

一个打包好的Java Web应用应有如下的目录结构，以便部署到Tomcat、Weblogic等容器中。

     WebRoot/					    
        css/							
        images/                     
        js/						
        logs/						
        META-INF/						
        WEB-INF/					
            classes/
            lib/				    
            web.xml		
        index.jsp
        404.jsp
        500.jsp

项目开发的目录结构就真没有规范可寻了，最简单的只需要一个src目录和一个WebRoot目录即可搞定；但随着时间推移，或许是半年，一年，也或许是两年，这样的目录结构并不能满足需求。 于是经过调整，可能会发展成这样：

    my_project/
        src/
            java源码包，一般按域名继续划分，防止包冲突，如 com.egolife.ssh；
        test/
            java测试源码包；
        resource/
            各类资源或配置文件，如struts, spring, system properties, freemarker templates, jbpm processes；
        doc/
            项目文档目录；
        lib/        
            测试时需要的额外的库，如jsp,servlet,junit,spring等；运行时需要的lib在WebRoot下；
            单独列出此lib，方便正式部署时排出这些包；
        reports/
            报告目录，如单元测试报告；
        WebRoot/
            Web根目录，包含运行所需的web.xml，lib，classes等；
        build.xml - Ant build文件；

但也可能会是这样：

    my_project/
        src/
            java源码包，一般按域名继续划分，防止包冲突，如 com.egolife.ssh；
        test/
            java测试源码包；
        config/
            各类资源或配置文件，如struts, spring, system properties, freemarker templates, jbpm processes；
        lib/        
            测试时需要的额外的库，如jsp,servlet,junit,spring等；运行时需要的lib在WebRoot下；
            单独列出此lib，方便正式部署时排出这些包；
        sql/ 
            数据库schema，或者实用的script；
        WebRoot/
            Web根目录，包含运行所需的web.xml，lib，classes等；
        
####Rails

Rails框架已经约定好了项目的目录结构，你只需要输入 `rails new my_app`，它就会自动帮你生成，每个文件/目录的定义清晰可见。

    my_app/
        app/
            Model, view, and controller files go here.
        bin/
            Wrapper scripts
        config/
            Configuration and database connection par
        config.ru - Rack server configuration.
        db/
            Schema and migration information.
        Gemfile - Gem Dependencies.
        lib/
            Shared code.
        log/
            Log files produced by your application.
        public/
            Web-accessible directory.
        Rakefile - Build script.
        README.rdoc - Installation and usage information.
        test/
            Unit, functional, and integration tests, fixtures
        tmp/
            Runtime temporary files.
        vendor/
            Imported code.

###包或模块结构

除了项目的顶级目录结构，包或模块结构的划分往往是一件令人头疼的事儿。

最早开始注意到这个问题，还是在11年工作后开发第一个Java Web应用时。那是四个人的小团队针对老系统进行再次开发，抱着动大刀的心态， 总觉得原有项目的包结构十分别扭，修改一个模块时经常需要跨越多个包，而且前端还使用了Adode Flex 3的框架，IDE提供的Refactor功能顿 时失灵了，在修改service的一个方法名、model的一个属性时别提会有多么恶心（深受其害之后动手写了一个小工具，可以批量将Java的Model映射成 Flex的valueObject，copy->paste->fix这种方式实在太ugly）。当然，很有可能是再次开发增强了这种恶心感，手里拿着锤 子什么的，那自然一切都成了钉子。不过，开发第二个Java Web项目时，还是沿用了原有 的包结构，SSH框架，前端由Adobe Flex 3换成了Ext JS3，但明显没有以前那种恶心感。如果这个系统再由一批新人去维护，很有可能他们也会受罪，正如我们一样，只不过这次是我们制造的。

言归正传，还是谈谈Web项目的包或模块结构，先引一篇老文，[JavaEye](http://www.iteye.com)新闻月刊2008年07月总第05期[四个有害的Java习惯之包的命名和划分](http://www.javaeye.com/news/3058)。

####包的命名和划分

包(package)的命名和划分按照行为和层次划分(package-by-layer)，而不是根据特征和功能划分(package-by-feature)

这个问题在我刚学java的时候就遇到了，在看了众多的网上开源程序后，我也慢慢习惯了按层次命名包。

作者举了个例子:

    com.blah.action
    com.blah.dao
    com.blah.model
    com.blah.util

我们已经习惯了按照层次分类或者叫按照行为分类，model一个包，dao一个包，service一个包，action一个 包。这样就把具有同样特征或者功能的类划分到了不同的包里。这样的习惯，把java的包内私有(package- private)这个作用域给完全扔掉了，而包内私有是java的默认作用域（ps:我学java来好像很少用过java的包内 私有这个作用域，汗一个）。

这种包的划分习惯也违反了面向对象编程的核心原则之--尽量保持私有以减少影响,因为这种习惯强迫你必须扩大类的作用域.

下面的包命名方式是按照特征划分命名:

    com.blah.painting
    com.blah.buyer
    com.blah.seller
    com.blah.auction
    com.blah.webmaster
    com.blah.useraccess
    com.blah.util

举个例子，在一个web应用中，`com.blah.painting` 包可能包含下面的成员:

    Painting.java: model对象
    PaintingDAO.java: dao对对象
    PaintingAction.java: controller or action 对象
    statements.sql: SQL文件
    view.jsp: JSP文件

值得注意的是这种情况下，包里包含的不仅仅是java源码文件，同时也包含其他与该特征相关的文件。这点上好像违反大多数java程序员的习惯，并且如果要打包为jar好像也不方便，真实环境中如何应用，有没有别的麻烦，还要待实践一下。

作者列举了这种包划分方式的优点:

* 包是高内聚的，并且模块化，包与包之间的耦合性被降到最低。
* 代码的自文档性(或自描述性 self-documenting)增强. 读者只需看包的名字就对程序有些什么功能或特 征有了大概的印象。在《代码大全》中, Steve McConnell 将自文档化(self-documenting)的代码比作 "the Holy Grail of legibility."(不知道怎么翻译)
* 把类按照每个特征和功能区分开可以很容易实现分层设计。
* 相关的成员在同一个位置。不需要为了编辑一个相关的成员而去浏览整个源码树。
* 成员的作用域默认是包内私有。只有当另外的包需要访问某个成员的时候，才把它修改为public. (需要 注意的是修改一个类为public，并不意味着它的所有类成员都应该改为public。public成员和包内私有 (package-private)成员是可以在同一个类里共存的。)
* 删除一个功能或特征只需要简单的删除一个文件夹。
* 每个包内一般只有很少的成员，这样包可以很自然的按照进化式发展。如果包慢慢变的太大，就可以再 进行细分，把它重构为两个或者更多新的包，类似于物种进化。而按照层次划分的方式，就没办法进化 式发展，重构也不容易。

作者引用了一句Effective Java中的名言:

	"The single most important factor that distinguishes a well-designed module from a poorly designed one is the degree to which the module hides its internal data and other implementation details from other modules." 

	-- Joshua Bloch, Effective Java
    
####Java, Rails and Django

在按照行为和层次划分还是根据特征和功能划分的争论上，我们的Java项目优先选择了前者，在MVC层级的结构之下再按特征和功能划分模块；Rails与之类似。那么，有没有反过来的呢，即正如上文作者提到的建议，先按特征和功能划分，再按行为和层次划分。答案是
Django，在Django 1.5.3 Documentation中提到的项目结构：

    tutorial/
        mysite/
            __init__.py
            settings.py
            urls.py
            wsgi.py
        polls/
            __init__.py
            urls.py
            views.py
            models.py
            admin.py
            tests.py
            static/
                polls/
                    style.css
            templates/
                404.html
                500.html
                polls/
                    detail.html
                    index.html
                    result.html
        hn/
            __init__.py
            urls.py
            views.py
            models.py
            admin.py
            tests.py
            static/
                hn/
                    style.css
            templates/
                404.html
                500.html
                hn/
                    detail.html
                    index.html
                    result.html
        templates/
            admin/
                base_site.html
        manage.py
		
目录结构，包结构十分重要，它们从文件、模块的层次体现着项目的设计水平和权衡，在这方面感觉Ruby和Django要略胜一筹，因为设计或不设计，它就在那里。

---	
	
##命名规范    

对程序猿来说，Coding并非是最难的事情；那是什么？命名！！！对，是命名偷走程序猿的大把时间和精力。

记得在一个OA项目开始初期，整理过一分Java和Ext JS的编码规范，其中命名规范是重点，实践起来实际上是困难重重。想一想，单是找出一个合适的英文单词 似乎就要绞尽脑汁，随意和不杀脑细胞的后果是瞅瞅国内一些开放平台的API就知道他们的英语水平和设计素养；当然，如果你直接使用中文编程就另当别论了。

###Java

Java命名规范举例（参考了AWDR4）

Model Naming

    Table           image_sprite    
    Package         com.egolife.ssh.po.media
    Class           ImageSprite
    File            my_project/src/com/egolife/ssh/po/media/ImageSprite.java
    ORM             my_project/src/com/egolife/ssh/hbm/media/ImageSprite.hbm.xml

Service Naming

    Package         com.egolife.ssh.service.media
    Interface       ImageSpriteService
    Method          ImageSprite findById(String id);
    File            my_project/src/com/egolife/ssh/service/media/ImageSpriteService.java
    
    Class           ImageSpriteServiceImpl
    Method          public ImageSprite findById(Srting id){ ... ... }
    File            my_project/src/com/egolife/ssh/service/media/impl/ImageSpriteServiceImpl.java    
    
    Spring          <bean id="ImageSpriteDAO" class="com.egolife.ssh.dao.media.ImageSpriteDAO">
                        <property name="sessionFactory">
                            <ref bean="sessionFactory" />
                        </property>
                    </bean>
                    
                    <bean id="imageSpriteService" class="com.egolife.ssh.service.media.ImageSpriteService">
                        <property name="imageSpriteDAO" ref="ImageSpriteDAO"/>
                    </bean>
                    
                    <bean  id="imageSpriteAction" class="com.egolife.ssh.action.media.ImageSpriteAction">
                        <property name="imageSpriteService" ref="imageSpriteService"/>
                    </bean>
                    
    File            my_project/resource/spring/applicationContext-media.xml
    
Action Naming

    URL             http://../media/findImageSpriteById.action?id=DEADBEEF
    Package         com.egolife.ssh.action.media
    Class           ImageSpriteAction
    Property        private String id;
    Method          public String findImageSpriteById(){ ... ...}
    File            my_project/src/com/egolife/ssh/action/media/ImageSpriteAction.java    
    
    Struts          <action name="*" class="imageSpriteAction" method="{1}">
                        <result type="json"></result>
                    </action>
    File            my_project/resource/struts/struts-media.xml    

除了Java文件，还涉及到Struts, Hibernate, Spring一堆XML的配置文件，当然，你也可以使用Annotation实现“零配置”。
    
###Rails

Rails命名规范举例（直接引用AWDR4）：All these conventions are shown in the following tables.

Model Naming

    Table           line_items
    File            app/models/line_item.rb
    Class           LintItem

Controller Naming

    URL             http://../store/list
    File            app/controllers/store_controller.rb
    Class           StoreController
    Method          list
    Layout          apps/views/layouts/store.html.erb

View Naming

    URL             http://../store/list
    File            app/views/store/list.html.erb (or .builder)
    Helper          module StoreHelper
    File            app/helpers/store_helper.rb
    
###ORM 命名策略

由于关系数据库与面向对象的不匹配，ORM应运而生。在Java中比较典型的ORM框架是Hibernate，采用XML文件描述Java POJO和数据库表之间的对应关系， 可以让开发人员以面向对象的方式来完成Java与数据库的交互，而不再纠缠于JDBC，写大量的原生SQL和参数的setter/getter；是的，这时最满意的要数程序员的 手指头。在Rails中，ActiveRecord担任了此角色，但省去了XML文件，这时你会更觉满意。

随着ORM的出现，Model和Table的命名问题也逐渐浮出水面：

* Table: line_item, line_items, or tb_line_items ?
* Id:    id, line_item_id, or line_items_id ?
* Model: LineItem or LineItems ?

在以SSH框架为基础的Java Web项目开发中，一般有两种选择：

* ddl2java：先进行数据库设计，然后通过逆向工程生成Java代码，包括Model, XML, DAO, 甚至是Service。此时Java层的命名由数据库层决定。
* java2ddl: 标准的面向对象设计，手写Model, XML，或直接使用Annotation，然后通过正向工程生成数据库DDL。此时数据库层的命名由Java层决定。

在接触过的项目中，以ddl2java的选择居多，逆向工程可以帮忙生成很多代码，这是自底向上的设计思路。

无论是ddl2java，还是java2ddl，都有一个叫[NamingStrategy](http://docs.jboss.org/hibernate/orm/3.2/api/org/hibernate/cfg/NamingStrategy.html)的工具 在帮你进行一些默认的转换，毕竟Java和数据库各有各的命名规范，迁就哪一个都觉得有所不妥。

在Rails中同样有NamingStragety，只不过这是一个很隐匿的家伙，约定俗成以至于不需要它了。

关于Model和Table的命名问题，最大的要数单数还是复数了。Java Web开发中暂未确定，随开发人员高兴，但一般还是挺一致的，要么都采用单数，要么都采用复数， 但这样又似乎确凿有些别扭：

* Singular: User(Class) -> user(Table)，表user有多条记录，每个记录代表一个User，也就是多个User，这样表名用user是否有些不妥？
* Plurals : Users(Class) -> users(Table)，表users有多条记录，每个记录代表一个User，似乎比上面好多了。但1）根据id查找用户时，应返回null或者User，此时却是Users，是多个用户吗，有点奇怪？ 2）模糊查找时返回List，此时却`List<Users>`，Users不是已经是复数了吗，这时你不会有一种使用foreach嵌套循环的冲动？这样似乎也有些不妥？

终极方案似乎是这样的：

* Mixing: User(Class) -> users(Table)，但此时需要你自定义Hibernate的NamingStragety，谁有时间去干这事儿；再说满足需求就行了，这事儿谁在意呢。

这问题在AWDR4中解释得很好，摘抄如下：
    
	David says: Why Plurals for Tables?

	Because it sounds good in conversation. Really. “Select a Product from products.” And “Order has_many :line_items.”

	The intent is to bridge programming and conversation by creating a domain language that can be shared by both. Having such a language means cutting down on the mental translation that otherwise confuses the discussion of a product description with the client when it’s really implemented as merchandise body. These communica- tions gaps are bound to lead to errors.

	Rails sweetens the deal by giving you most of the configuration for free if you follow the standard conventions. Developers are thus rewarded for doing the right thing, so it’s less about giving up “your ways” and more about getting productivity for free.

---
	
##日志处理

先讲一个笑话，第一次见到[Log4j](http://logging.apache.org/log4j/)，你会怎么读？"Log|Four|J"，还是"Log|四|J"？饱受中文和阿拉伯汉子熏陶的Java程序猿，若是第一次碰到，不出意外，大都 会读错，即读成 "Log|四|J"，在我不长的Java开发生涯里，已经碰到好几例。

即使联想到"J"是"Java"的缩写，也难以想到"4"代表什么；但若知道这世上还有Log4cxx，Log4php，那大概可以猜到"4"其实代表"For"，只是"LogForJava"写起来太长了，"Java"缩写成"J"，"For"干脆就用"4"代替了；更进一步，可以说Log4j所代表的是一种思想、一种设计，只不过刚好是Java语言的实现。 这和"B2B"、"B2C"是一个道理，但君不见也有某主持人把"B2B"读成"B二B"的。

调试Java程序，难免会有打印输出，使用`System.out.println(message)`和`System.err.println(error)`就可以满足需求；但你一定干过这事儿：1）第一版的代码里为了调试写满println，调试好后觉得输出的无关信息太多，看着怪怪的，手痒了就非常勤快地把它们删掉；但使用时还是莫名地出错，于是又手贱地再写了一遍`println`。 2）正式上线前，经理突然说把项目里的调试代码注释掉，以免影响运行的性能；好家伙，这一天没写一行代码，反倒删除了几千行。

这时，Log4j可以帮你免除手痒手贱之苦。使用Log4j可以自定义输出级别，方便控制项目在测试阶段、上线运行时的日志输出；你也可以在日志输出到标准输出的同时，保存一份到文件或数据库中，以便定时查看和统计分析；碰到Error/Fatal类的错误时，发送一封日志邮件给开发维护人员也很不错，何乐而不为呢。

Log4j是很多Java程序里默认的日志组件，在Hibernate逆向工程生成的DAO里即可找到它的身影。看起来很不错，但要在自己的Java代码用到，还是得稍微花点功夫。这时你需要引入Log4j的配置，熟悉rootLogger、LogLevel、Appender、Layout等概念，若有兴趣，似乎也想看下Log4j的设计原理和具体实现，趁机“Pick Up”一些设计模式， 然后为己所用。不仔细看文档，直接上配置和代码的人可能要折腾一小会儿了，好在打造一份Log4j.properties之后，就可以随你“Copy and Paste”。

Rails中有类似的日志组件，叫Logger -- supporting rollover，零配置即可用；当然了，遇到项目上线运行时还是需要定制下的。只是在此不得不感叹下，在Rails中使用Logger似乎出乎天性、理所当然，但Log4j却要一些折腾，一些配置。

Gists：

* [Log4j Gist](https://gist.github.com/dylanninin/7426118)

---

##单元测试

在最初的Java Web开发里，是没有单元测试的概念的，即使到现在开发人员也依然习惯说：功能我写好了，你看！

jUnit是什么？为什么要单元测试？即使我看了jUnit in Action，理解测试的重要性，也不见得会按部就班的进行严格的单元测试。

在Java Web项目中，可以借助IDE自动生成单元测试用例，虽然功能有限，但也省了不少时间（如果连这个功能都不知道，那可以说你还生活在原始时代）。 出于对IDE自动生成的单元测试用例的不满，自己写过两个版本的小工具。一个是Java版的，粗野的将文本扫描和正则表达式相结合，渲染freeMarker模板，批量生成 TestCase和Tests，并自动填充Parameters和Asserts，接下来所要做的工作就是更改Parameters和Asserts，并运行测试即可。第二个是Python版的，最初是想用Java重写，但还是 脱离不了扫描源文件（想过使用反射来实现，但看Java提供的反射API，运行时源代码中定义的参数名丢失了，实在不忍用arg1, arg2来代替start, pageSize），当时正好在学Python， 所以改用Python重新实现。代码只能捂脸见人，所以就不贴出来了，思路在模板，见[jUnit TestCase Gist](https://gist.github.com/dylanninin/7426041)。

对涉及到数据交互的单元测试，jUnit已经不够用了。当时找到一个叫DbUnit的小框架，是jUnit的扩展，可以用XML事先构建一些测试数据集，在单元测试的时候载入数据库， 测试完成后从数据库中清除，有效的控制了测试数据库的状态。使用DbUnit大概有两个好处：1）构建测试数据集，可重复测试，再也不用担心测试数据被修改或丢失；2）测试完成后清除测试数据，保证了测试前后数据库的数据是一致的。
    
当然，使用jUnit已经很折腾，加上DbUnit，好像又得花几天的时间了。

那么，Rails中是怎么解决的呢？

Rails提供了scaffold和generator，可以自动生成测试用例，而且把我想通过编写小工具去实现的功能完成得更加优雅；在构建测试数据时，Rails一致地选择了YAML，对了，这应该称作Fixtures，你可以在test/fixtures目录下找到它们。

YAML是什么呢，YAML is a recursive acronym for "YAML Ain't Markup Languade". Early in its development, YAML was said to mean "Yet Another Markup Language", but it was then reinterpreted(backronyming the original acronym) to distinguish its purpose as data-oriented, rather than document markup. 详情请见[Wikipedia: YAML](http://en.wikipedia.org/wiki/YAM)。

为什么不使用XML，因为YAML面向数据、自解释，你再也不用写一堆标签和属性。

这还不是最重要的，最重要的是，在这种内在的测试支持的帮助下，你会很乐于做这件事而无需额外折腾，正文AWDR4文中所言“One of the real joys of the Rails framework is that it has support for testing baked right in from the start of every project.”

##构建工具

Java中用于自动化构建的工具有Ant和Maven。Ant起步比较麻烦，需要手写一大堆东西；Maven无需配置，可直接上手使用。但Maven的网络特性更强一些，在隔离互联网的内网开发环境下是难以生存的，所以要用也只用到Ant。

Ant的介绍：Apache Ant is a Java library and command-line tool whose mission is to drive processes described in build files as targets and extension points dependent upon each other. The main known usage of Ant is the build of Java applications. Ant supplies a number of built-in tasks allowing to compile, assemble, test and run Java applications. Ant can also be used effectively to build non Java applications, for instance C or C++ applications. More generally, Ant can be used to pilot any type of process which can be described in terms of targets and tasks.

Ant可以编译、打包、测试和运行Java程序，但不限于此，你还可以编写自己的扩展，加入到Ant Lib中，实现更多更丰富的任务，比如创建Java项目的目录和包结构；一些开源的项目也提供了Ant Lib，比如Hibernate，jUnit。

从头开始写一个Ant配置有点麻烦，但写好之后基本可以复用，有不一样的地方只需根据项目需求进行调整即可，这样似乎有点一劳永逸了，也似乎有点不够优雅，更别提创建一个新项目的时候你还记得有这事儿吗？踩进与Ant有点关系的深坑，要数实习期间的一个Web项目，前端使用Adobe Flex 3， 在给MyEclipse装上一大堆插件之后，编译Flex代码变得奇慢无比；若是你不小心勾选了自动编译的选项，Flex代码的任何一点改动都可以让你等上一二十分钟。这时想到了Ant，查到Ant和Adobe Flex的官网，确实提供有编译Flex的Lib，也有一些教程，接下来就是测试和移植工作了。那会儿顿时觉得很兴奋， 希望一天内就能完成，实际上零零散散花了一周多的时间还没搞定，记得好像是某些style资源始终无法编译到SWF，最后就不了了之。

Gists：

* [Ant Gist](https://gist.github.com/dylanninin/7425918)
* [Flex with Ant Gist](https://gist.github.com/dylanninin/7425972)

那么Rails表现如何呢？Rails提供了Rake，比起Ant需从头编写build.xml以及使用Flex Task时遇到的困难，Rake更像Maven，内置了很多任务，无需配置；到目前为止，我还没踩进Rake的坑。

Rake的介绍：Rake is like having a reliable assistant on hand all the time: you tell it to do some task, and that task gets done. 

Rake在你键入"rails new my_apps"时，已经陪伴你左右，随时待命。见[Rake Gist](https://gist.github.com/dylanninin/7431140)。

是的，Rake是一个值得信赖的好助手，随时随地就在身边供你差遣；而Ant需要你手工打造，好与坏完全取决于自身的水平。

##参考

* [Agile Web Development with Rails 4](http://book.douban.com/subject/24718727/)
* [四个有害的Java习惯之包的命名和划分](http://www.javaeye.com/news/3058)
