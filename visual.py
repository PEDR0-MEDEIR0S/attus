# -----------------------------------------------------------------------------
# Script: bpmn_fluxo_dispensa_recurso_modelado.py
# Descrição: Gera um diagrama de processo (fluxo BPMN simplificado) utilizando
#            a biblioteca Graphviz, representando o fluxo de dispensa de recurso
#            judicial no âmbito do Núcleo de Saúde do Ministério Público.
# Objetivo: Modelar visualmente as etapas e decisões envolvidas na análise de
#           uma intimação judicial, desde o recebimento até a conclusão da demanda.
# -----------------------------------------------------------------------------
from graphviz import Digraph



bpmn = Digraph('BPMN', format='png')
bpmn.attr(rankdir='TB', splines='ortho', nodesep='0.6', ranksep='0.75')

with bpmn.subgraph(name='cluster_1') as pb:
    pb.attr(label='Procurador de Base\n(Núcleo de Saúde)', style='filled', color='lightgrey')
    pb.node('start', 'Início: Recebe intimação judicial', shape='circle', style='filled', fillcolor='white')
    pb.node('analisa', 'Analisa decisão judicial\n(entende que não cabe recurso)', shape='box')
    pb.node('sol_chefe', 'Solicita aprovação ao\nProcurador Chefe', shape='box')
    pb.node('notificado', 'Recebe decisão (Deferida ou Indeferida)', shape='box')
    pb.node('fim', 'Conclui demanda', shape='circle', style='filled', fillcolor='white')

with bpmn.subgraph(name='cluster_2') as chefe:
    chefe.attr(label='Procurador Chefe\n(Núcleo de Saúde)', style='filled', color='lightblue')
    chefe.node('dec_chefe', 'Decide: Aprova ou Encaminha\npara Subprocuradoria', shape='diamond')
    chefe.node('resp_pb', 'Notifica Procurador de Base', shape='box')

with bpmn.subgraph(name='cluster_3') as sub:
    sub.attr(label='Subprocuradoria', style='filled', color='lightyellow')
    sub.node('dec_sub', 'Decide: Aprova ou Encaminha\npara Gabinete', shape='diamond')
    sub.node('resp_chefe', 'Notifica Procurador Chefe', shape='box')

with bpmn.subgraph(name='cluster_4') as gabinete:
    gabinete.attr(label='Gabinete do Procurador-Geral', style='filled', color='lightpink')
    gabinete.node('dec_gab', 'Analisa e Decide', shape='box')
    gabinete.node('ret_sub', 'Retorna decisão à\nSubprocuradoria', shape='box')

bpmn.edge('start', 'analisa')
bpmn.edge('analisa', 'sol_chefe')
bpmn.edge('sol_chefe', 'dec_chefe')
bpmn.edge('dec_chefe', 'resp_pb', label='Aprova')
bpmn.edge('dec_chefe', 'dec_sub', label='Encaminha')
bpmn.edge('dec_sub', 'resp_chefe', label='Aprova')
bpmn.edge('dec_sub', 'dec_gab', label='Encaminha')
bpmn.edge('dec_gab', 'ret_sub')
bpmn.edge('ret_sub', 'resp_chefe')
bpmn.edge('resp_chefe', 'resp_pb')
bpmn.edge('resp_pb', 'notificado')
bpmn.edge('notificado', 'fim')

bpmn.render('esquema_utilizado_para_bpmn', view=True)
