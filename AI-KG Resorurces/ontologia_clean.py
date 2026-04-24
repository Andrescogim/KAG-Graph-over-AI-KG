CLASES = """
Material :"An object that is processed, used, or returned by methods in order to pursue a task. In computer science it is typically  a data set, a knowledge base, or a system. Some examples include ‘vocabulary', 'biometric data', 'Wordnet', and 'social network'." ;

Metric :"A measure of quantitative assessment, commonly used for comparing or assessing the performance of a method.  Some examples include ‘word error rate', 'minimum classification error', 'normalized mutual information', and 'fault exposure ratio'." ;

OtherEntity :"A significant entity that we were unable to classify as task, method, metric, or material. It usually refers to real world entities that are used by or affect tasks and methods. Some examples include ‘password’, ‘keyboard’, ‘fingerprint’, and ‘pixel’." ;

Method :"A specific approach, usually adopted to address a task.  Some examples include ‘neural networks’, decision trees’, ‘principal component analysis’, ‘support vector machine’, and ‘fuzzy logic’." ;

Task :"A piece of work to carry out, usually to solve a specific challenge. Some examples include ‘knowledge discovery’, ‘dimensionality reduction’, ‘computer vision’, and ‘authentication’." ;
"""


RELACIONES = """

- evaluatesMaterial: indicates that an instance belonging to one class in { Metric } evaluates an instance of  Material.  It is inferred from the following predicates : 'evaluate'." ;

- evaluatesMethod: indicates that an instance belonging to one class in { Metric } evaluates an instance of  Method.  It is inferred from the following predicates : 'evaluate'." ;

- evaluatesMetric: indicates that an instance belonging to one class in { Metric } evaluates an instance of  Metric.  It is inferred from the following predicates : 'evaluate'." ;

- evaluatesOtherEntity: indicates that an instance belonging to one class in { Metric } evaluates an instance of  OtherEntity.  It is inferred from the following predicates : 'evaluate'." ;

- evaluatesTask: indicates that an instance belonging to one class in { Metric } evaluates an instance of  Task.  It is inferred from the following predicates : 'evaluate'." ;

- improvesMethod: indicates that an instance belonging to one class in { Material, Method, OtherEntity, Task } improves an instance of  Method. It is inferred from all the following predicates : 'improve', 'evolve', 'grown', 'enrich', 'expand', 'augment', 'update', 'change', 'raise', 'increase', 'enhance', 'advance', 'gain'." ;

- improvesMetric: indicates that an instance belonging to one class in { Method, OtherEntity, Task } improves an instance of  Metric. It is inferred from all the following predicates : 'improve', 'evolve', 'grown', 'enrich', 'expand', 'augment', 'update', 'change', 'raise', 'increase', 'enhance', 'advance', 'gain'." ;

- improvesTask: indicates that an instance belonging to one class in { Method, OtherEntity, Task } improves an instance of  Task. It is inferred from all the following predicates : 'improve', 'evolve', 'grown', 'enrich', 'expand', 'augment', 'update', 'change', 'raise', 'increase', 'enhance', 'advance', 'gain'." ;

- includesMaterial: indicates that an instance belonging to one class in { Material, Method, OtherEntity } includes an instance of  Material.  It is inferred from the following predicates : 'include', 'represent', 'contain', 'comprise', 'comprise', 'cover', 'consider', 'incorporate'. " ;

- includesMethod: indicates that an instance belonging to one class in { Method, Task } includes an instance of  Method.  It is inferred from the following predicates : 'include', 'represent', 'contain', 'comprise', 'comprise', 'cover', 'consider', 'incorporate'. " ;

- includesOtherEntity: indicates that an instance belonging to one class in { Material, Method, OtherEntity } includes an instance of  OtherEntity.  It is inferred from the following predicates : 'include', 'represent', 'contain', 'comprise', 'comprise', 'cover', 'consider', 'incorporate'. " ;

- includesTask: indicates that an instance belonging to one class in { Task } includes an instance of  Task.  It is inferred from the following predicates : 'include', 'represent', 'contain', 'comprise', 'comprise', 'cover', 'consider', 'incorporate'. " ;

- predictsMaterial: indicates that an instance belonging to one class in { Method, OtherEntity, Task } predicts an instance of  Material. It is inferred from all the following predicates : 'predict', 'forecast', 'derive'. " ;

- predictsMetric: indicates that an instance belonging to one class in { Method, Metric, OtherEntity, Task } predicts an instance of  Metric. It is inferred from all the following predicates : 'predict', 'forecast', 'derive'. " ;

- predictsOtherEntity: indicates that an instance belonging to one class in { Method, Metric, OtherEntity, Task } predicts an instance of  OtherEntity. It is inferred from all the following predicates : 'predict', 'forecast', 'derive'. " ;

- providesMaterial: indicates that an instance belonging to one class in { Method, OtherEntity, Task } provides an instance of  Material. It is inferred from all the following predicates : 'provide', 'distribute', 'have', 'offer', 'exhibit', 'achieve', 'yield', 'deliver', 'provide', 'give', 'add', 'produce', 'generate', 'build', 'create', 'design', 'design', 'manufacture', 'establish', 'develop', 'implement', 'deploy', 'make', 'construct', 'realize'" ;

- requiresMaterial: indicates that an instance belonging to one class in { Method, Task } requires an instance of  Material. It is inferred from all the following predicates : 'require', 'need', 'demand'." ;

- requiresTask: indicates that an instance belonging to one class in { Method, Task } requires an instance of  Task. It is inferred from all the following predicates : 'require', 'need', 'demand'." ;

- supportsMethod: indicates that an instance belonging to one class in { Method, OtherEntity, Task } supports an instance of  Method. It is inferred from all the following predicates : 'support', 'underlie', 'enable', 'assist', 'promote', 'help', 'empower', 'facilitate', 'aid', 'foster', 'facilitate', 'allow', 'solve'. " ;

- supportsOtherEntity: indicates that an instance belonging to one class in { Material, Method, Task } supports an instance of  OtherEntity. It is inferred from all the following predicates : 'support', 'underlie', 'enable', 'assist', 'promote', 'help', 'empower', 'facilitate', 'aid', 'foster', 'facilitate', 'allow', 'solve'. " ;

- supportsTask: indicates that an instance belonging to one class in { Material, Method, Metric, OtherEntity, Task } supports an instance of  Task. It is inferred from all the following predicates : 'support', 'underlie', 'enable', 'assist', 'promote', 'help', 'empower', 'facilitate', 'aid', 'foster', 'facilitate', 'allow', 'solve'. " ;

- usesMaterial: indicates that an instance belonging to one class in { Method, Task } uses an instance of  Material.  It is inferred from the following predicates : 'use', 'utilise', 'employ', 'utilize', 'exploit', 'integrate', 'adopt', 'leverage', 'apply', 'involve', 'rely'." ;

- usesMethod: indicates that an instance belonging to one class in { Method, OtherEntity, Task } uses an instance of  Method.  It is inferred from the following predicates : 'use', 'utilise', 'employ', 'utilize', 'exploit', 'integrate', 'adopt', 'leverage', 'apply', 'involve', 'rely'." ;

- usesMetric: indicates that an instance belonging to one class in { Method, OtherEntity, Task } uses an instance of  Metric.  It is inferred from the following predicates : 'use', 'utilise', 'employ', 'utilize', 'exploit', 'integrate', 'adopt', 'leverage', 'apply', 'involve', 'rely'." ;

- usesOtherEntity: indicates that an instance belonging to one class in { Method, Metric, OtherEntity, Task } uses an instance of  OtherEntity.  It is inferred from the following predicates : 'use', 'utilise', 'employ', 'utilize', 'exploit', 'integrate', 'adopt', 'leverage', 'apply', 'involve', 'rely'." ;

- usesTask: indicates that an instance belonging to one class in { Task } uses an instance of  Task.  It is inferred from the following predicates : 'use', 'utilise', 'employ', 'utilize', 'exploit', 'integrate', 'adopt', 'leverage', 'apply', 'involve', 'rely'." ;


"""

RELACIONES_INVERSAS = """

aikg-ont:OtherEntityEvaluatedBy
    rdfs:comment "This relation indicates that an instance	 of class OtherEntity was evaluated by an instance belonging to one of the following classes { Metric }.  It is inferred from the Evaluate-for relationships extracted by the DyGIE++ classifier and the following predicates extracted by the NLP pipeline: 'evaluate'." ;
    rdfs:domain aikg-ont:OtherEntity ;
    rdfs:range _:N8c5d4098f1ea439392756c16bcec1081 ;
    owl:inverseOf aikg-ont:evaluatesOtherEntity .

aikg-ont:OtherEntityIncludedBy
    rdfs:comment "This relation indicates that an instance	 of class OtherEntity was included by an instance belonging to one of the following classes { Material, Method, OtherEntity }.  It is inferred from the Feature-of and Part-of relationships extracted by the DyGIE++ classifier and the following predicates extracted by the NLP pipeline: 'include', 'represent', 'contain', 'comprise', 'comprise', 'cover', 'consider', 'incorporate'. " ;
    rdfs:domain aikg-ont:OtherEntity ;
    rdfs:range _:N1f9f891ce35e4e39a3eebf95e0aac2b8 ;
    owl:inverseOf aikg-ont:includesOtherEntity .

aikg-ont:OtherEntityPredictedBy
    rdfs:comment "This relation indicates that an instance	 of class OtherEntity was predicted by an instance belonging to one of the following classes { Method, Metric, OtherEntity, Task }. It is inferred from all the following predicates extracted by the NLP pipeline: 'predict', 'forecast', 'derive'. " ;
    rdfs:domain aikg-ont:OtherEntity ;
    rdfs:range _:N6368cae504eb43a69ddeed4266249678 ;
    owl:inverseOf aikg-ont:predictsOtherEntity .

aikg-ont:OtherEntitySupportedBy
    rdfs:comment "This relation indicates that an instance	 of class OtherEntity was supported by an instance belonging to one of the following classes { Material, Method, Task }. It is inferred from all the following predicates extracted by the NLP pipeline: 'support', 'underlie', 'enable', 'assist', 'promote', 'help', 'empower', 'facilitate', 'aid', 'foster', 'facilitate', 'allow', 'solve'. " ;
    rdfs:domain aikg-ont:OtherEntity ;
    rdfs:range _:N7726d2ca774844d3bd98f3fb67ef2901 ;
    owl:inverseOf aikg-ont:supportsOtherEntity .

aikg-ont:OtherEntityUsedBy
    rdfs:comment "This relation indicates that an instance	 of class OtherEntity was used by an instance belonging to one of the following classes { Method, Metric, OtherEntity, Task }.  It is inferred from the Used-for relationships extracted by the DyGIE++ classifier and the following predicates extracted by the NLP pipeline: 'use', 'utilise', 'employ', 'utilize', 'exploit', 'integrate', 'adopt', 'leverage', 'apply', 'involve', 'rely'." ;
    rdfs:domain aikg-ont:OtherEntity ;
    rdfs:range _:Nd1af4677ee264f61b94cb61dddf9cd1d ;
    owl:inverseOf aikg-ont:usesOtherEntity .


aikg-ont:materialEvaluatedBy
    rdfs:comment "This relation indicates that an instance	 of class Material was evaluated by an instance belonging to one of the following classes { Metric }.  It is inferred from the Evaluate-for relationships extracted by the DyGIE++ classifier and the following predicates extracted by the NLP pipeline: 'evaluate'." ;
    rdfs:domain aikg-ont:Material ;
    rdfs:range _:N60f5878755944519be40a45bc6c52659 ;
    owl:inverseOf aikg-ont:evaluatesMaterial .

aikg-ont:materialIncludedBy
    rdfs:comment "This relation indicates that an instance	 of class Material was included by an instance belonging to one of the following classes { Material, Method, OtherEntity }.  It is inferred from the Feature-of and Part-of relationships extracted by the DyGIE++ classifier and the following predicates extracted by the NLP pipeline: 'include', 'represent', 'contain', 'comprise', 'comprise', 'cover', 'consider', 'incorporate'. " ;
    rdfs:domain aikg-ont:Material ;
    rdfs:range _:N1c812aac0637431395e3a1e064232b56 ;
    owl:inverseOf aikg-ont:includesMaterial .

aikg-ont:materialPredictedBy
    rdfs:comment "This relation indicates that an instance	 of class Material was predicted by an instance belonging to one of the following classes { Method, OtherEntity, Task }. It is inferred from all the following predicates extracted by the NLP pipeline: 'predict', 'forecast', 'derive'. " ;
    rdfs:domain aikg-ont:Material ;
    rdfs:range _:N583bb6e5948d461c89495f4e067c56bb ;
    owl:inverseOf aikg-ont:predictsMaterial .

aikg-ont:materialProvidedBy
    rdfs:comment "This relation indicates that an instance	 of class Material was provided by an instance belonging to one of the following classes { Method, OtherEntity, Task }. It is inferred from all the following predicates extracted by the NLP pipeline: 'provide', 'distribute', 'have', 'offer', 'exhibit', 'achieve', 'yield', 'deliver', 'provide', 'give', 'add', 'produce', 'generate', 'build', 'create', 'design', 'design', 'manufacture', 'establish', 'develop', 'implement', 'deploy', 'make', 'construct', 'realize'" ;
    rdfs:domain aikg-ont:Material ;
    rdfs:range _:N33ba5cd4887448f581694fe8c4a3d561 ;
    owl:inverseOf aikg-ont:providesMaterial .

aikg-ont:materialRequiredBy
    rdfs:comment "This relation indicates that an instance	 of class Material was required by an instance belonging to one of the following classes { Method, Task }. It is inferred from all the following predicates extracted by the NLP pipeline: 'require', 'need', 'demand'." ;
    rdfs:domain aikg-ont:Material ;
    rdfs:range _:N69dbdc7e2f064df198f9e0d972fccefa ;
    owl:inverseOf aikg-ont:requiresMaterial .

aikg-ont:materialUsedBy
    rdfs:comment "This relation indicates that an instance	 of class Material was used by an instance belonging to one of the following classes { Method, Task }.  It is inferred from the Used-for relationships extracted by the DyGIE++ classifier and the following predicates extracted by the NLP pipeline: 'use', 'utilise', 'employ', 'utilize', 'exploit', 'integrate', 'adopt', 'leverage', 'apply', 'involve', 'rely'." ;
    rdfs:domain aikg-ont:Material ;
    rdfs:range _:N69deda1d3c014566b5d87f265b2c9e0d ;
    owl:inverseOf aikg-ont:usesMaterial .

aikg-ont:methodEvaluatedBy
    rdfs:comment "This relation indicates that an instance	 of class Method was evaluated by an instance belonging to one of the following classes { Metric }.  It is inferred from the Evaluate-for relationships extracted by the DyGIE++ classifier and the following predicates extracted by the NLP pipeline: 'evaluate'." ;
    rdfs:domain aikg-ont:Method ;
    rdfs:range _:N22d13ea7e4204e1f98a307b3d3cafb26 ;
    owl:inverseOf aikg-ont:evaluatesMethod .

aikg-ont:methodImprovedBy
    rdfs:comment "This relation indicates that an instance	 of class Method was improved by an instance belonging to one of the following classes { Material, Method, OtherEntity, Task }. It is inferred from all the following predicates extracted by the NLP pipeline: 'improve', 'evolve', 'grown', 'enrich', 'expand', 'augment', 'update', 'change', 'raise', 'increase', 'enhance', 'advance', 'gain'." ;
    rdfs:domain aikg-ont:Method ;
    rdfs:range _:N414420914e3144bf9b32fafa98388d13 ;
    owl:inverseOf aikg-ont:improvesMethod .

aikg-ont:methodIncludedBy
    rdfs:comment "This relation indicates that an instance	 of class Method was included by an instance belonging to one of the following classes { Method, Task }.  It is inferred from the Feature-of and Part-of relationships extracted by the DyGIE++ classifier and the following predicates extracted by the NLP pipeline: 'include', 'represent', 'contain', 'comprise', 'comprise', 'cover', 'consider', 'incorporate'. " ;
    rdfs:domain aikg-ont:Method ;
    rdfs:range _:N353ed147f6454d9bb33252e908dd68fe ;
    owl:inverseOf aikg-ont:includesMethod .

aikg-ont:methodSupportedBy
    rdfs:comment "This relation indicates that an instance	 of class Method was supported by an instance belonging to one of the following classes { Method, OtherEntity, Task }. It is inferred from all the following predicates extracted by the NLP pipeline: 'support', 'underlie', 'enable', 'assist', 'promote', 'help', 'empower', 'facilitate', 'aid', 'foster', 'facilitate', 'allow', 'solve'. " ;
    rdfs:domain aikg-ont:Method ;
    rdfs:range _:N6fd9031ec650424988d8e873dd8c9c0a ;
    owl:inverseOf aikg-ont:supportsMethod .

aikg-ont:methodUsedBy
    rdfs:comment "This relation indicates that an instance	 of class Method was used by an instance belonging to one of the following classes { Method, OtherEntity, Task }.  It is inferred from the Used-for relationships extracted by the DyGIE++ classifier and the following predicates extracted by the NLP pipeline: 'use', 'utilise', 'employ', 'utilize', 'exploit', 'integrate', 'adopt', 'leverage', 'apply', 'involve', 'rely'." ;
    rdfs:domain aikg-ont:Method ;
    rdfs:range _:Ne244540e4c624ebd98dd8cadb382279f ;
    owl:inverseOf aikg-ont:usesMethod .

aikg-ont:metricEvaluatedBy
    rdfs:comment "This relation indicates that an instance	 of class Metric was evaluated by an instance belonging to one of the following classes { Metric }.  It is inferred from the Evaluate-for relationships extracted by the DyGIE++ classifier and the following predicates extracted by the NLP pipeline: 'evaluate'." ;
    rdfs:domain aikg-ont:Metric ;
    rdfs:range _:Ncceef75337db44fca5cd866e8102a03c ;
    owl:inverseOf aikg-ont:evaluatesMetric .

aikg-ont:metricImprovedBy
    rdfs:comment "This relation indicates that an instance	 of class Metric was improved by an instance belonging to one of the following classes { Method, OtherEntity, Task }. It is inferred from all the following predicates extracted by the NLP pipeline: 'improve', 'evolve', 'grown', 'enrich', 'expand', 'augment', 'update', 'change', 'raise', 'increase', 'enhance', 'advance', 'gain'." ;
    rdfs:domain aikg-ont:Metric ;
    rdfs:range _:N563ff1d949084879af5868a35860f27f ;
    owl:inverseOf aikg-ont:improvesMetric .

aikg-ont:metricPredictedBy
    rdfs:comment "This relation indicates that an instance	 of class Metric was predicted by an instance belonging to one of the following classes { Method, Metric, OtherEntity, Task }. It is inferred from all the following predicates extracted by the NLP pipeline: 'predict', 'forecast', 'derive'. " ;
    rdfs:domain aikg-ont:Metric ;
    rdfs:range _:Nad1055ca4bce4217b9eb5aaae0a1e713 ;
    owl:inverseOf aikg-ont:predictsMetric .

aikg-ont:metricUsedBy
    rdfs:comment "This relation indicates that an instance	 of class Metric was used by an instance belonging to one of the following classes { Method, OtherEntity, Task }.  It is inferred from the Used-for relationships extracted by the DyGIE++ classifier and the following predicates extracted by the NLP pipeline: 'use', 'utilise', 'employ', 'utilize', 'exploit', 'integrate', 'adopt', 'leverage', 'apply', 'involve', 'rely'." ;
    rdfs:domain aikg-ont:Metric ;
    rdfs:range _:Nb6c2f27bbdbb4597bee2d5d90de41132 ;
    owl:inverseOf aikg-ont:usesMetric .

aikg-ont:taskEvaluatedBy
    rdfs:comment "This relation indicates that an instance	 of class Task was evaluated by an instance belonging to one of the following classes { Metric }.  It is inferred from the Evaluate-for relationships extracted by the DyGIE++ classifier and the following predicates extracted by the NLP pipeline: 'evaluate'." ;
    rdfs:domain aikg-ont:Task ;
    rdfs:range _:N37c331ea1cfb4f9cb3acce3ba2fa9352 ;
    owl:inverseOf aikg-ont:evaluatesTask .

aikg-ont:taskImprovedBy
    rdfs:comment "This relation indicates that an instance	 of class Task was improved by an instance belonging to one of the following classes { Method, OtherEntity, Task }. It is inferred from all the following predicates extracted by the NLP pipeline: 'improve', 'evolve', 'grown', 'enrich', 'expand', 'augment', 'update', 'change', 'raise', 'increase', 'enhance', 'advance', 'gain'." ;
    rdfs:domain aikg-ont:Task ;
    rdfs:range _:N504b2e937467493bb60c069b182eec80 ;
    owl:inverseOf aikg-ont:improvesTask .

aikg-ont:taskIncludedBy
    rdfs:comment "This relation indicates that an instance	 of class Task was included by an instance belonging to one of the following classes { Task }.  It is inferred from the Feature-of and Part-of relationships extracted by the DyGIE++ classifier and the following predicates extracted by the NLP pipeline: 'include', 'represent', 'contain', 'comprise', 'comprise', 'cover', 'consider', 'incorporate'. " ;
    rdfs:domain aikg-ont:Task ;
    rdfs:range _:N74d7738b54a545e5807de8fc91f5bde5 ;
    owl:inverseOf aikg-ont:includesTask .

aikg-ont:taskRequiredBy
    rdfs:comment "This relation indicates that an instance	 of class Task was required by an instance belonging to one of the following classes { Method, Task }. It is inferred from all the following predicates extracted by the NLP pipeline: 'require', 'need', 'demand'." ;
    rdfs:domain aikg-ont:Task ;
    rdfs:range _:Nccb299d54d504b009360594abd93918d ;
    owl:inverseOf aikg-ont:requiresTask .

aikg-ont:taskSupportedBy
    rdfs:comment "This relation indicates that an instance	 of class Task was supported by an instance belonging to one of the following classes { Material, Method, Metric, OtherEntity, Task }. It is inferred from all the following predicates extracted by the NLP pipeline: 'support', 'underlie', 'enable', 'assist', 'promote', 'help', 'empower', 'facilitate', 'aid', 'foster', 'facilitate', 'allow', 'solve'. " ;
    rdfs:domain aikg-ont:Task ;
    rdfs:range _:Ncbaeae8daf7b4eeb90dc80806dfbf55f ;
    owl:inverseOf aikg-ont:supportsTask .

aikg-ont:taskUsedBy
    rdfs:comment "This relation indicates that an instance	 of class Task was used by an instance belonging to one of the following classes { Task }.  It is inferred from the Used-for relationships extracted by the DyGIE++ classifier and the following predicates extracted by the NLP pipeline: 'use', 'utilise', 'employ', 'utilize', 'exploit', 'integrate', 'adopt', 'leverage', 'apply', 'involve', 'rely'." ;
    rdfs:domain aikg-ont:Task ;
    rdfs:range _:N8e864b5a3fbf458ebd0980a30fdf5253 ;
    owl:inverseOf aikg-ont:usesTask .

"""
