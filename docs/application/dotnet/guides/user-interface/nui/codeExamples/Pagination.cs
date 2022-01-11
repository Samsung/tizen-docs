using System;
using Tizen.NUI;
using Tizen.NUI.BaseComponents;
using Tizen.NUI.Components;

namespace NUIXamlSimpleApp
{
	public partial class XamlPage : ContentPage
	{
        public XamlPage()
        {
            InitializeComponent();
            Scroller.ScrollAnimationEnded += OnScrollAnimationEnded;
            PaginationStyle paginationStyle = new PaginationStyle()
            {
                IndicatorSize = new Size(26, 26),
                IndicatorSpacing = 8,
                IndicatorImageUrl = new Selector<string>
                {
                    Normal = ResourcePath + "pagination_ic_nor.png",
                    Selected = ResourcePath + "pagination_ic_sel.png"
                }
            };

            Index.ApplyStyle(paginationStyle);
            Index.BackgroundColor = Color.Gray;
            Index.IndicatorCount = 3;
            Index.SelectedIndex = 0;
        }
        private void OnScrollAnimationEnded(object sender, ScrollEventArgs args)
        {
            Index.SelectedIndex = Scroller.CurrentPage;
        }
	}
}
