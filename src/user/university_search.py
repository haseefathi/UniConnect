from project.project_data_paths import paths
import pandas as pd
from fuzzywuzzy import process
from matplotlib.pyplot import figure
from matplotlib.legend import Legend
from bokeh.embed import components

def university_search(query):


    data_file_path = paths['university_admissions_data']
    names = ['University', 'Major', 'Degree', 'Season', 'Decision', 'GPA',
             'Verbal', 'Quant', 'AWA', 'TOEFL']

    

    names = ['University', 'Major', 'Degree', 'Season', 'Decision', 'GPA',
             'Verbal', 'Quant', 'AWA', 'TOEFL']

    df = pd.read_csv(data_file_path, names=names, header=None)

    if query is not None:

        universities = df.University

        total_universities_list = []
        for university in universities:
            if university not in total_universities_list:
                total_universities_list.append(university)

        # university_name.to_csv('all_universities_list.csv')
        final_university = process.extractOne(query, total_universities_list)
        if final_university[1] < 80:
            query = None
        else:
            query = final_university[0]

        print ('ok here', query)

    df1 = df[df['University'] == query]
    df2 = df1[(df1['Decision'] == 'Accepted')]

    # print df2
    if df2 is not None:

        df2['GRE_Scores'] = (df2[['Verbal', 'Quant']].sum(axis=1))

        avg_gre = (df2['GRE_Scores'].dropna()).mean()
        average_gre = float("%.2f" % avg_gre)
        min_gre = (df2['GRE_Scores'].dropna()).min()
        max_gre = (df2['GRE_Scores'].dropna()).max()

        average_gre_verbal = (df2['Verbal'].dropna()).mean()
        min_gre_verbal = (df2['Verbal'].dropna()).min()
        max_gre_verbal = (df2['Verbal'].dropna()).max()

        average_gre_quant = (df2['Quant'].dropna()).mean()
        min_gre_quant = (df2['Quant'].dropna()).min()
        max_gre_quant = (df2['Quant'].dropna()).max()

        avg_gpa = (df2['GPA'].dropna()).mean()
        average_gpa = float("%.2f" % avg_gpa)
        min_gpa = (df2['GPA'].dropna()).min()
        max_gpa = (df2['GPA'].dropna()).max()

        avg_toefl = (df2['TOEFL'].dropna()).mean()
        average_toefl = float("%.2f" % avg_toefl)
        min_toefl = (df2['TOEFL'].dropna()).min()
        max_toefl = (df2['TOEFL'].dropna()).max()

        total_accepted = df1[df1['Decision'] == 'Accepted'].Decision.count()
        total_rejected = df1[df1['Decision'] == 'Rejected'].Decision.count()
        total_wait_listed = df1[df1['Decision'] == 'Wait listed'].Decision.count()
        total_interview = df1[df1['Decision'] == 'Interview'].Decision.count()
        total_other_decision = df1[df1['Decision'] == 'Other'].Decision.count()

        accept_rate = float((total_accepted/float(total_accepted + total_rejected +
                                total_wait_listed + total_interview + total_other_decision)))
        acceptance_rate = float("%.2f" % (accept_rate*100))

        majors = df1.Major

        final_majors = []
        for i in majors:
            if i not in final_majors:
                final_majors.append(i)

        total_majors = len(final_majors)

        # def create_graph_for_scores(average, max, min, min_range, max_range):

        #     plot = figure(plot_width=600, plot_height=350, y_range=(min_range, max_range))

        #     bar1 = plot.vbar(x=[1], width=0.5, bottom=0, top=[average], color=["blue"], alpha=0.7)

        #     bar2 = plot.vbar(x=[2], width=0.5, bottom=0, top=[max], color=["green"], alpha=0.7)

        #     bar3 = plot.vbar(x=[3], width=0.5, bottom=0, top=[min], color=["red"], alpha=0.7)

        #     plot.yaxis.axis_label = "GRE Scores"

        #     legend = Legend(items=[
        #         ("AVERAGE", [bar1]),
        #         ("MAXIMUM", [bar2]),
        #         ("MINIMUM", [bar3]),
        #     ], location=(0, -30))

        #     plot.add_layout(legend, 'right')

        #     script, div = components(plot, CDN)

        #     return script, div

        # graph_for_gre = create_graph_for_scores(average_gre, max_gre, min_gre, min_range=260, max_range=340)
        # graph_for_gpa = create_graph_for_scores(average_gpa, max_gpa, min_gpa, min_range=0, max_range=4)
        # graph_for_toefl = create_graph_for_scores(average_toefl, max_toefl, min_toefl, min_range=20, max_range=120)

        # data = pd.Series([acceptance_rate, float(1-acceptance_rate)], index=['Acceptance Rate', 'Rejection Rate'])
        # plot = Donut(data)
        #
        # script, div = components(plot, CDN)

        # # define starts/ends for wedges from percentages of a circle
        # percents = [0, acceptance_rate, 100-acceptance_rate]
        # starts = [p * 2 * pi for p in percents[:-1]]
        # ends = [p * 2 * pi for p in percents[1:]]
        #
        # # a color for each pie piece
        # colors = ["yellow", "red"]
        #
        # plot = figure(x_range=(-1, 1), y_range=(-1, 1), plot_width=430, plot_height=360)
        #
        # plot.wedge(x=0, y=0, radius=0.80, start_angle=starts, end_angle=ends, color=colors, alpha=0.7)
        #
        # script, div = components(plot, CDN)


        context = {
            # 'script_for_gpa': graph_for_gpa[0],
            # 'div_for_gpa': graph_for_gpa[1],
            # 'script_for_toefl': graph_for_toefl[0],
            # 'div_for_toefl': graph_for_toefl[1],
            # 'script_for_gre': graph_for_gre[0],
            # 'div_for_gre': graph_for_gre[1],
            # 'script': script,
            # 'div': div,
            'university_name': query,
            'acceptance_rate': acceptance_rate,
            'average_gre': average_gre,
            'min_gre': min_gre,
            'max_gre': max_gre,
            'average_gre_verbal': average_gre_verbal,
            'average_gre_quant': average_gre_quant,
            'average_gpa': average_gpa,
            'total_majors': total_majors,
            'final_majors': final_majors,
            'min_gre_verbal': min_gre_verbal,
            'max_gre_verbal': max_gre_verbal,
            'min_gre_quant': min_gre_quant,
            'max_gre_quant': max_gre_quant,
            'min_gpa': min_gpa,
            'max_gpa': max_gpa,
            'average_toefl': average_toefl,
            'min_toefl': min_toefl,
            'max_toefl': max_toefl
        }
    else:
        context = {
            'error_message': True
        }
    return context